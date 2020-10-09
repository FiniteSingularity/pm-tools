import yfinance as yf
from pandas_datareader import data as pdr
import numpy as np
import pandas as pd

from .models import Symbol, Price

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
    for date, row in holdings_th.iterrows():
        Price.objects.create(
            ticker=symbol_d,
            date=date,
            open_price=int(row['Open']*100),
            close_price=int(row['Close']*100),
            low_price=int(row['Low']*100),
            high_price=int(row['High']*100),
            adjusted_close=int(row['Adj Close']*100),
            volume=int(row['Volume']/1000)
        )
    return symbol_d