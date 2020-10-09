from django.db import models
from pmtoolsapi.symbols.models import Symbol
import pandas as pd

# Create your models here.

class Benchmark(models.Model):
    name = models.CharField(max_length=255)
    ticker = models.ForeignKey(Symbol, on_delete=models.CASCADE)

    def calculate_beta(self, equity, num_days=756):
        rows = (num_days+1)
        eq_pr = equity.price_history.all().order_by('date')
        bench_pr = self.ticker.price_history.all().order_by('date')
        eq_adj = [p.adjusted_close/100 for p in eq_pr][-rows:]
        bench_adj = [p.adjusted_close/100 for p in bench_pr][-rows:]
        df = pd.DataFrame({'equity': eq_adj, 'bench': bench_adj})
        df['equity_dr']=df['equity'].pct_change()
        df['bench_dr']=df['bench'].pct_change()
        beta = df['equity_dr'].cov(df['bench_dr'])/df['bench_dr'].var()
        return beta
    
    def calculate_er(self, equity, bench_er, num_days):
        beta = self.calculate_beta(equity, num_days)
        return beta * bench_er