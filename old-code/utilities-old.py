import numpy as np
import pandas as pd

def portfolio_sigma(weights, daily_returns):
    w = weights.to_numpy()
    cov = daily_returns.cov().to_numpy()
    return np.sqrt((w.dot(cov)).dot(w.T) * 252)

def multi_portfolio_sigma(weights, daily_returns):
    w = weights.to_numpy()
    cov = daily_returns.cov().to_numpy()
    return np.sqrt((w.dot(cov) * w).sum(-1) * 252)

def portfolio_expected_return(weights, expected_returns):
    w = weights.to_numpy()
    E = expected_returns[weights.columns].to_numpy()
    return w.dot(E.T)

def generate_random_weights(n_portfolios, n_holdings):
    w = np.random.uniform(size=(n_portfolios, n_holdings))
    return w/w.sum(axis=1)[:,None]
