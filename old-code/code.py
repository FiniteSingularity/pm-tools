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
    portfolio_sigma,
    generate_random_weights,
    multi_portfolio_sigma
)

#%%
market = ['SPY']
portfolio = [
    'AAPL',
    'GE',
    'TSLA',
    'CLX',
    'SBUX',
    'JNJ',
    'PG',
    'CRM',
    'SHOP',
    'ROKU',
    'SHW',
    'ECL',
    'MKC',
    'LOW',
    'GWW',
    'DIS'
]

weights = np.random.uniform(size=(1,16))
w_df = pd.DataFrame(weights/weights.sum(), columns=portfolio)
print(w_df)
# %%
yf.pdr_override()
holdings_data = pdr.get_data_yahoo(portfolio)
adj_close = holdings_data['Adj Close'][portfolio]
market_data = pdr.get_data_yahoo(market)
market_adj_close = market_data['Adj Close']

#%%
holdings_dr = (adj_close.pct_change()).iloc[-756:]
market_dr = (market_adj_close.pct_change()).iloc[-756:]

# %%
expected_market_return = 0.10
CAPM = get_capm(holdings_dr, market_dr, expected_market_return)

# %%
er = portfolio_expected_returns(w_df, CAPM['Er'])
print('er: {}'.format(er))
# %%
sigma = portfolio_sigma(w_df, holdings_dr) * np.sqrt(252)
print('sigma: {}'.format(sigma))

# %%
w = generate_random_weights(10000, 16)
W = pd.DataFrame(w, columns=holdings_dr.columns)
print(W)
# %%
ers = portfolio_expected_returns(W, CAPM['Er'])

# %%
sigmas = multi_portfolio_sigma(W, holdings_dr) * np.sqrt(252)

port_data = pd.DataFrame({'sigma': sigmas, 'er': ers})
print(port_data)
# %%

f, ax = plt.subplots(figsize=(11,9))
sns.scatterplot(data=port_data, x="sigma", y="er")
# %%
