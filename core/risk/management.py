class RiskManager:
    def __init__(self, capital=100000, max_risk=0.02):
        self.capital = capital
        self.max_risk = max_risk
        
    def calculate_position(self, entry, stop, atr):
        risk_amount = self.capital * self.max_risk
        risk_per_contract = abs(entry - stop) + 2*atr
        return max(int(risk_amount / risk_per_contract), 1)
    
    def pyramiding_allowed(self, current_pnl):
        return current_pnl > self.capital * 0.005  # 0.5% profit