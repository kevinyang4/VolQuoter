# VolQuoter
Reinforcement Learning for Volatility-Aware Options Market Making

# VolQuoter
Reinforcement Learning for Volatility‑Aware Options Market Making

VolQuoter is a hybrid quant research and trading project that simulates an options market microstructure and trains a reinforcement learning market maker to quote bid/ask spreads and hedge inventory under stochastic volatility. This project demonstrates research, strategy implementation, and production-ready code—all in one package, suitable for quant research, trading, and development roles.

## Features
- Custom market simulation environment (`env/`) for options trading.
- Black-Scholes and Poisson order flow modeling for realistic trading dynamics.
- RL agent training (PPO) for inventory and spread management.
- Backtesting and metrics evaluation for both naive and RL-based strategies.
- Jupyter notebooks for exploratory data analysis and signal testing.
- Streamlit dashboard for interactive simulations.

## Quickstart
```bash
# 1) Create virtual environment
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Train a small PPO agent
python agent/train_ppo.py --episodes 10 --steps 2000

# 4) Run a quick demo rollout
python demo.py

# 5) (Optional) Launch interactive dashboard
streamlit run dashboard/app.py
```

## Project Structure
```
VolQuoter/
├── data/                  # Market data: raw and processed
├── notebooks/             # EDA and model exploration notebooks
├── src/                   # Core modules: env, strategy, backtester, utils
├── agent/                 # RL agent training and evaluation
├── tests/                 # Unit tests for core modules
├── demo.py                # Quick demo script
├── dashboard/             # Streamlit dashboard
├── requirements.txt       # Python dependencies
├── README.md              # Project overview and instructions
└── .gitignore             # Ignored files
```

## Usage
- Use `notebooks/` for research, signal testing, and experimentation.
- Train agents via `agent/train_ppo.py`.
- Evaluate strategies using `scripts/evaluate.py`.
- Visualize results with `dashboard/app.py` or `src/visualization.py`.
- Extend the environment (`src/env/`) to implement more sophisticated models or multi-asset simulations.


## Next Steps / Extensions
- Expand to multiple options and maturities.
- Implement stochastic volatility models (Heston, SABR).
- Integrate live market data for pseudo-live backtesting.
- Add more sophisticated reward functions, risk constraints, or transaction costs.
