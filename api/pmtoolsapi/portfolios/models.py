import pandas as pd

from django.db import models
from pmtoolsapi.symbols.models import Symbol
from pmtoolsapi.benchmarks.models import Benchmark

# Create your models here.

class ModelPortfolio(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_symbols_th(self, symbols, num_trading_days):
        data = pd.DataFrame()
        for sym in symbols:
            qs = sym.price_history.all().order_by('date')
            df = qs.to_timeseries(
                fieldnames=['date', 'adjusted_close'], index='date', coerce_float=True
            )
            data[sym.ticker] = df['adjusted_close']
        return data.iloc[-num_trading_days:]

    def get_holdings_th(self, num_trading_days=756):
        holdings = self.holdings.all().values_list('holding', flat=True)
        symbols = Symbol.objects.filter(pk__in=holdings)
        return self.get_symbols_th(symbols, num_trading_days)

    def get_bencharks_th(self, num_trading_days=756):
        benchmarks = self.benchmarks.all()
        symbol_ids = [benchmark.benchmark.ticker_id for benchmark in benchmarks]
        symbols = Symbol.objects.filter(pk__in=symbol_ids)
        return self.get_symbols_th(symbols, num_trading_days)

    def cov(self, num_trading_days=756):
        data = self.get_holdings_th(num_trading_days)
        dr = data.pct_change()
        return dr.cov()

    def corr(self, num_trading_days=756):
        data = self.get_holdings_th(num_trading_days)
        dr = data.pct_change()
        return dr.corr()

    def expected_returns(self, num_trading_days=756):
        pass
    
    def betas(self, num_trading_days=756):
        holdings_th = self.get_holdings_th(num_trading_days)
        holdings_dr = holdings_th.pct_change()
        benchmarks_th = self.get_bencharks_th(num_trading_days)
        benchmarks_dr = benchmarks_th.pct_change()
        holding_benchmarks = {}
        
        for holding in self.holdings.all():
            holding_benchmarks[holding.holding.ticker] = holding.benchmark.ticker.ticker

        betas = {}
        for symbol in holdings_th.columns:
            bench_symbol = holding_benchmarks[symbol]
            beta = holdings_dr[symbol].cov(benchmarks_dr[bench_symbol])/benchmarks_dr[bench_symbol].var()
            betas[symbol] = beta    

        return betas

class ModelPortfolioHolding(models.Model):
    portfolio = models.ForeignKey(ModelPortfolio, on_delete=models.CASCADE, related_name='holdings')
    holding = models.ForeignKey(Symbol, on_delete=models.PROTECT, related_name='portfolio_holdings')
    weight = models.FloatField(default=0.0)
    benchmark = models.ForeignKey(Benchmark, on_delete=models.PROTECT, related_name='portfolio_holdings')

    def __str__(self):
        return f"{self.holding.ticker} [{self.benchmark.ticker.ticker}]: {self.weight}"

class ModelPortfolioBench(models.Model):
    portfolio = models.ForeignKey(ModelPortfolio, on_delete=models.CASCADE, related_name='benchmarks', null=True)
    benchmark = models.ForeignKey(Benchmark, on_delete=models.PROTECT, related_name='benchmarks')
    expected_return = models.FloatField(default=0.0)