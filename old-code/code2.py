#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
from utilities import (
    get_betas,
    get_capm,
    portfolio_expected_returns,
    multi_portfolio_sigma,
    portfolio_sigma,
    generate_random_weights,
    calc_holding_returns,
    mvo
)
from portfolio import portfolio, benchmarks

yf.pdr_override()

holdings = pd.DataFrame(portfolio).fillna(0.0)
holdings['min_weight'] = 0.0
holdings['max_weight'] = 1.0

print('---- Downloading Ticker Data ----')
holdings_th = pdr.get_data_yahoo(holdings['symbol'].tolist())['Adj Close'][holdings['symbol'].tolist()]
holdings_dr = holdings_th.pct_change()[-756:]
holdings_cov = holdings_dr.cov()

benchmarks = pd.DataFrame(benchmarks).set_index('symbol')
benchmarks_th = pdr.get_data_yahoo(benchmarks.index.tolist())['Adj Close'][benchmarks.index.tolist()]
benchmarks_dr = benchmarks_th.pct_change()[-756:]

#%%
print('---- Calculating Expected Returns ----')
holdings = calc_holding_returns(holdings, benchmarks, holdings_dr, benchmarks_dr)

print('---- Generating 10000 random portfolios ----')
w = generate_random_weights(10000, len(holdings))
W = pd.DataFrame(w, columns=holdings_dr.columns)
holdings_er = holdings['Er']
holdings_er.index = holdings['symbol']
ers_rand = portfolio_expected_returns(W, holdings_er)
sigmas_rand = multi_portfolio_sigma(W, holdings_dr) * np.sqrt(252)
rand_ports = pd.DataFrame({'sigma': sigmas_rand, 'er': ers_rand})

print('---- Calculating Efficient Frontier ----')
sigmas, er, ports = mvo(holdings, holdings_dr)

frontier = pd.DataFrame({'sigma': sigmas, 'er': er})

f, ax = plt.subplots()
sns.lineplot(data=frontier, x="sigma", y="er", ax=ax)
sns.scatterplot(data=rand_ports, x="sigma", y="er", ax=ax)