import pandas as pd

class SwingDetector:
    def __init__(self, reversal_percent=1.0):
        self.reversal = reversal_percent / 100

    def detect_swings(self, df):
        """Gann-style swing point detection"""
        swings = []
        current_high = df['High'].iloc[0]
        current_low = df['Low'].iloc[0]
        
        for idx, row in df.iterrows():
            if row['High'] > current_high * (1 + self.reversal):
                swings.append(('high', idx, row['High']))
                current_high = row['High']
            elif row['Low'] < current_low * (1 - self.reversal):
                swings.append(('low', idx, row['Low']))
                current_low = row['Low']
                
        return pd.DataFrame(swings, columns=['type', 'date', 'price'])