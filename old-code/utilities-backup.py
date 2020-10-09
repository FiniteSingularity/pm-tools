import numpy as np
import pandas as pd
from cvxopt import matrix
from cvxopt.blas import dot
from cvxopt.solvers import qp, options
from scipy.interpolate import interp1d


def get_betas(holdings_dr, market_dr):
    return (pd.concat([holdings_dr, market_dr], axis=1).cov()['Adj Close'].iloc[0:-1]/market_dr.var()).to_frame('beta')


def get_capm(holdings_dr, market_dr, expected_return):
    CAPM = get_betas(holdings_dr, market_dr)
    CAPM['Er'] = CAPM['beta']*expected_return
    return CAPM


def portfolio_expected_returns(weights, expected_returns):
    w = weights.to_numpy()
    E = expected_returns[weights.columns].to_numpy()
    return w.dot(E.T)


def portfolio_sigma(weights, daily_returns):
    w = weights.to_numpy()
    cov = daily_returns.cov().to_numpy()
    return np.sqrt((w.dot(cov)).dot(w.T))


def generate_random_weights(n_portfolios, n_holdings):
    w = np.random.uniform(size=(n_portfolios, n_holdings))
    return w/w.sum(axis=1)[:, None]


def multi_portfolio_sigma(weights, daily_returns):
    w = weights.to_numpy()
    cov = daily_returns.cov().to_numpy()
    return np.sqrt((w.dot(cov) * w).sum(-1))


def calc_holding_returns(holdings, benchmarks, holdings_dr, benchmarks_dr):
    betas = []
    ers = []
    for index, row in holdings.iterrows():
        symbol = row['symbol']
        bench_symbol = row['bench']
        beta = holdings_dr[symbol].cov(
            benchmarks_dr[bench_symbol])/benchmarks_dr[bench_symbol].var()
        er = beta * benchmarks.loc[bench_symbol]['ER']
        betas.append(beta)
        ers.append(er)
    holdings['beta'] = betas
    holdings['Er'] = ers
    return holdings


def mvo(holdings, holdings_dr):
    n = len(holdings)
    returns = holdings['Er'].to_numpy()
    bounds = np.hstack(
        [(-1.0*holdings['min_weight']).tolist(), holdings['max_weight'].tolist()])
    G = np.vstack([-np.eye(n), np.eye(n)])
    Sig = holdings_dr.cov().to_numpy()
    sigmas, er, ports = solve_mvo(Sig, returns, bounds, G, 500)
    sigmas = sigmas * np.sqrt(252)
    return sigmas, er, ports


def solve_mvo(Sig, R, bounds, G, resolution=2000, points=100):
    n = len(Sig)
    S = matrix(np.asarray(Sig))
    pbar = matrix(np.asarray(R))
    G = matrix(G)
    h = matrix(bounds.flatten())
    A = matrix(1.0, (1, n))
    b = matrix(1.0)

    N = resolution
    mus = [10**(10.0*t/N - 1.0) for t in reversed(range(N))]
    options['show_progress'] = False
    xs = []
    risks = []
    returns = []
    last_insert = -999999999.9
    min_delta = 0.0001

    for mu in mus:
        x = qp(mu*S, -pbar, G, h, A, b)['x']
        risk = np.sqrt(dot(x, S*x))
        if abs(risk - last_insert) > min_delta:
            xs.append(np.array(x).flatten())
            returns.append(dot(pbar, x))
            risks.append(risk)
            last_insert = risk

    xs = np.array(xs)
    sigmas = np.linspace(min(risks), max(risks), points)
    er = np.interp(sigmas, risks, returns)
    f = interp1d(np.array(risks), xs.T)
    ports = f(sigmas).T

    return sigmas, er, ports
