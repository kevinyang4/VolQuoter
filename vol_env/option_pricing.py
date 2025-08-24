import numpy as np
from scipy.stats import norm

# Black-Scholes (no divs) for quick refs

def _d1_d2(S, K, T, r, sigma):
    if T <= 0 or sigma <= 0 or S <= 0 or K <= 0:
        return np.inf, np.inf
    vol_sqrt = sigma * np.sqrt(T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / vol_sqrt
    d2 = d1 - vol_sqrt
    return d1, d2

def bs_call_price(S, K, T, r, sigma):
    if T <= 0:
        return max(S - K, 0.0)
    d1, d2 = _d1_d2(S, K, T, r, sigma)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def bs_put_price(S, K, T, r, sigma):
    if T <= 0:
        return max(K - S, 0.0)
    d1, d2 = _d1_d2(S, K, T, r, sigma)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def bs_delta_call(S, K, T, r, sigma):
    if T <= 0:
        return 1.0 if S > K else 0.0
    d1, _ = _d1_d2(S, K, T, r, sigma)
    return norm.cdf(d1)

def bs_delta_put(S, K, T, r, sigma):
    return bs_delta_call(S, K, T, r, sigma) - 1.0