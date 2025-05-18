import telegram
from functools import wraps

class AlertSystem:
    def __init__(self):
        self.bot = telegram.Bot(token="YOUR_BOT_TOKEN")
        self.chat_id = "YOUR_CHAT_ID"
        
    def alert_limiter(func):
        """Prevent alert flooding"""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if time.time() - self.last_alert > 60:  # 1 min cooldown
                return func(self, *args, **kwargs)
        return wrapper
    
    @alert_limiter
    def send_alert(self, message):
        self.bot.send_message(
            chat_id=self.chat_id,
            text=f"🚨 OIL ALERT: {message}"
        )