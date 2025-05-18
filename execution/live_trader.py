import ccxt
from core.risk.management import RiskManager

class BinanceTrader:
    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': 'YOUR_API_KEY',
            'secret': 'YOUR_SECRET',
            'enableRateLimit': True
        })
        self.risk = RiskManager()
        
    def execute_order(self, signal):
        if signal['confidence'] > 75:
            order = self.exchange.create_market_order(
                symbol='CL/FUTURES',
                side='buy' if signal['direction'] == 'long' else 'sell',
                amount=self.risk.calculate_position(
                    signal['entry'], 
                    signal['stop'],
                    signal['atr']
                )
            )
            return order
        return None