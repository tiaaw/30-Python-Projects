from datetime import datetime
from dataclass import dataclass 

@dataclass
class Habit: 
    name: str
    time_since: str
    remaining_days: str
    minutes_saved:str
    monet_saved: str
    
def track_habit(name: str, start: datetime, cost: float, minutes_used:float) -> Habit: