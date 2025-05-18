# Trading Parameters
SYMBOL = "CL=F"
TIMEFRAMES = ['1d', '4h', '1h']
RISK_PARAMS = {
    'max_daily_loss': 0.05,
    'position_sizing': 'volatility_based'
}

# Gann Settings
GANN = {
    'pivot_lookback': 14,
    'angle_calculation': 'dynamic'
}

# Data Sources
DATA_CONFIG = {
    'historical': 'yfinance',
    'live': 'binance'
}