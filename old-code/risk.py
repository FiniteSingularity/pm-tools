#%%

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

portfolio = [
    'AAPL',
    'GE',
    'TSLA',
    'CLX',
    'SBUX',
    'SPY',
    'BND',
    'BAB',
    'JNK',
    'WAVIX',
]

yf.pdr_override()
data = pdr.get_data_yahoo(portfolio)
adj_close = data['Adj Close'][portfolio]
dr = (adj_close/adj_close.shift(1) - 1.0).iloc[-756:]
cov = dr.cov()
corr = dr.corr()

# %%
f, ax = plt.subplots(figsize=(11,9))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr, cmap=cmap, vmax=1.0, vmin=-1.0, center=0, square=True, linewidths=0.5)

# %%
