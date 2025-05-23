from datetime import datetime
from dataclasses import dataclass
@dataclass
class Habit: 
    name: str
    time_since: str
    remaining_days: str
    minutes_saved:int
    money_saved: float
    
def track_habit(name: str, start: datetime, cost: float, minutes_used:float) -> Habit:
    goal = 60
    hourly_wage = 45
    
    # COnvert timestamp into hours and days
    time_elapsed = (datetime.now() - start).total_seconds()
    hours = round(time_elapsed / 3600, 1)
    days = round(hours / 24, 2)
    
    # Bonus details
    money_saved = cost * days
    mins_used = round(days * minutes_used)
    total_money_saved = round(money_saved + (minutes_used / 60 * hourly_wage), 2)
    
    days_to_go = round(goal - days)
    
    # Displayable information
    remaining_days = 'Cleared!' if days_to_go <- 0 else f'{days_to_go} days to go'
    time_since = f'{days} days' if hours > 72 else f'{hours} hours'
    
    return Habit(name=name,
                 time_since=time_since,
                 remaining_days=remaining_days,
                 minutes_saved=mins_used,
                 money_saved=total_money_saved)