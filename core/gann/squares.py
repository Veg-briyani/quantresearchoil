import math
from astropy.time import Time

class SquareOfNine:
    def __init__(self):
        self.seasonal_cycles = {
            'summer_driving': (5, 8),
            'winter_heating': (11, 2)
        }

    def calculate(self, price, date):
        """Integrated price-time square calculation"""
        jd = Time(date).jd % 365.25  # Annual cycle normalization
        
        price_sq = math.sqrt(price)
        time_sq = math.sqrt(jd)
        
        return {
            'price_root': round(price_sq, 4),
            'time_root': round(time_sq, 4),
            'confluence': abs(price_sq - time_sq) < 0.25,
            'seasonal': any(start <= date.month <= end 
                          for (start, end) in self.seasonal_cycles.values())
        }