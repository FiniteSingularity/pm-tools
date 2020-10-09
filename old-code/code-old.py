# %%
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
    portfolio_sigma,
    generate_random_weights,
    multi_portfolio_sigma,
    calc_holding_returns,
    mvo
)
from portfolio import portfolio, benchmarks

yf.pdr_override()

holdings = pd.DataFrame(portfolio).fillna(0.0)
holdings['min_weight'] = 0.01
holdings['max_weight'] = 0.08

print('---- Downloading ticker data ----')
holdings_th = pdr.get_data_yahoo(holdings['symbol'].tolist())['Adj Close']
holdings_dr = holdings_th.pct_change()[-756:]
holdings_cov = holdings_dr.cov()*np.sqrt(252)

benchmarks = pd.DataFrame(benchmarks).set_index('symbol')
benchmarks_th = pdr.get_data_yahoo(benchmarks.index.tolist())['Adj Close']
benchmarks_dr = benchmarks_th.pct_change()[-756:]

print('---- Calculating Expected Returns ----')
holdings = calc_holding_returns(
    holdings, benchmarks, holdings_dr, benchmarks_dr)

print('---- Generating 100k random portfolios ----')
w = generate_random_weights(100000, len(holdings))
W = pd.DataFrame(w, columns=holdings_dr.columns)
holdings_er = holdings['Er']
holdings_er.index = holdings['symbol']
ers_rand = portfolio_expected_returns(W, holdings_er)
sigmas_rand = multi_portfolio_sigma(W, holdings_dr) * np.sqrt(252)
rand_ports = pd.DataFrame({'sigma': sigmas_rand, 'er': ers_rand})

print('---- Calculating Efficient Frontier ----')
sigmas, er, ports = mvo(holdings, holdings_dr)

frontier = pd.DataFrame({'sigma': sigmas, 'er': er})

# %%

f, ax = plt.subplots()
sns.lineplot(data=frontier, x="sigma", y="er", ax=ax)
sns.scatterplot(data=rand_ports, x="sigma", y="er", ax=ax)

# %%
