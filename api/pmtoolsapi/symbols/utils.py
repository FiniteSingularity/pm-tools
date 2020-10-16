import datetime

import yfinance as yf
from pandas_datareader import data as pdr
import numpy as np
import pandas as pd

from django.db.models import Max

from .models import Symbol, Price

def update_yahoo_symbols():
    latest = Price.objects.all().values(
        'ticker__ticker'
    ).annotate(
        latest = Max('date')
    ).order_by('latest')
    data = {}
    for row in latest:
        date_str = row['latest'].strftime('%Y-%m-%d')
        if not date_str in data:
            data[date_str] = {'date': row['latest'], 'symbols': []}
        data[date_str]['symbols'].append(row['ticker__ticker'])
    for date, row in data.items():
        get_recent_pricing_from_yahoo(row['symbols'], row['date'])

def get_recent_pricing_from_yahoo(symbols, last_date):
    print(symbols)
    print(last_date)
    start_date = last_date + datetime.timedelta(days=1)
    try:
        data = pdr.get_data_yahoo(symbols, start=start_date)
        data = data.swaplevel(i=0, j=1, axis=1)
        price_data = []
        for ticker in symbols:
            sym = Symbol.objects.get(ticker=ticker)
            ticker_data = data[ticker]
            for date, row in ticker_data.iterrows():
                price_data.append(
                    Price(
                        ticker=sym,
                        date = date,
                        open_price=int(row['Open']*100),
                        close_price=int(row['Close']*100),
                        low_price=int(row['Low']*100),
                        high_price=int(row['High']*100),
                        adjusted_close=int(row['Adj Close']*100),
                        volume=int(row['Volume']/1000)
                    )
                )
        Price.objects.bulk_create(price_data, 1000)
    except:
        print('No data')

# TODO- Error handling if ticker doesn't exist at yahoo
def make_symbol_from_yahoo(ticker):
    sym = yf.Ticker(ticker)
    yf.pdr_override()
    info = sym.info
    short_name = info['shortName']
    long_name = info['longName']
    source = 'Y'
    symbol_d = Symbol.objects.create(
        short_name=short_name,
        long_name=long_name,
        ticker=ticker,
        source=source
    )
    holdings_th = pdr.get_data_yahoo(ticker)
    holdings_th = holdings_th.fillna(-1.0)

    price_data = [
        Price(
            ticker=symbol_d,
            date = date,
            open_price=row['Open'],
            close_price=row['Close'],
            low_price=row['Low'],
            high_price=row['High'],
            adjusted_close=row['Adj Close'],
            volume=row['Volume']
        ) for date, row in holdings_th.iterrows()
    ]
    Price.objects.bulk_create(price_data, 1000)
    return symbol_d