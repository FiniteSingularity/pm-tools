#%%

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

tickers = ["SPY", "AAPL", "XOM", "CLX"]
data = pdr.get_data_yahoo(tickers)
# %%
adj_close = data['Adj Close']
dr = (adj_close/adj_close.shift(1) - 1.0).iloc[-756:]

betas = (dr.cov()/dr['SPY'].var())['SPY']
print(betas)
# %%
total_returns = adj_close.iloc[-1]/adj_close.iloc[-756] - 1.0
print(total_returns)
capm_returns = betas * total_returns['SPY']
print(capm_returns)
# %%
rfr = 0.007
rf = (1.0+rfr) ** 3 - 1.0
print(rf)
alphas = total_returns - rf - betas * (total_returns['SPY'] - rf)
print(alphas)
# %%
