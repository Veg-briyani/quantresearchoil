import numpy as np
import pandas as pd

class GannCalculator:
    def __init__(self, volatility_window=14):
        self.vol_window = volatility_window
    
    def _find_pivots(self, high, low):
        """Identify swing highs/lows using volatility filter"""
        pivots = pd.DataFrame(index=high.index)
        pivots['high'] = high[(high > high.shift(1)) & (high > high.shift(-1))]
        pivots['low'] = low[(low < low.shift(1)) & (low < low.shift(-1))]
        return pivots.dropna()

    def calculate_angles(self, df):
        """Main Gann angle calculation method"""
        df = df.copy()
        pivots = self._find_pivots(df['High'], df['Low'])
        
        if len(pivots) < 2:
            raise ValueError("Insufficient pivots for angle calculation")
            
        last_high = pivots['high'].iloc[-1]
        last_low = pivots['low'].iloc[-1]
        price_range = last_high - last_low
        days = (pivots.index[-1] - pivots.index[-2]).days
        
        df['1x1'] = last_low + (df.index - pivots.index[-2]).days * (price_range/days)
        df['2x1'] = last_low + 2 * (df.index - pivots.index[-2]).days * (price_range/days)
        return df