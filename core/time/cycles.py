from pandas.tseries.holiday import USFederalHolidayCalendar

class OilCycles:
    def __init__(self):
        self.cal = USFederalHolidayCalendar()
        
    def get_seasonal_pattern(self, date):
        month = date.month
        if 3 <= month <= 5:
            return 'Spring Maintenance'
        elif 6 <= month <= 8:
            return 'Summer Demand'
        elif 9 <= month <= 11:
            return 'Autumn Inventory'
        return 'Winter Geopolitics'

    def get_report_dates(self, start, end):
        """Get EIA report Wednesdays"""
        dates = pd.date_range(start, end, freq='W-WED')
        return dates[dates.weekday == 2]  # Ensure Wednesdays