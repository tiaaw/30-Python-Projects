import pandas as pd 
from tabulate import tabulate
from datetime import datetime 
from habit_tracker import track_habit, Habit

def main(): 
    habits = [
        track_habit('Quit Coffee', datetime(2025, 5, 8, 8), cost = 4.5, minutes_used = 15),
        track_habit('Quit Smoking', datetime(2025, 2, 1, 8), cost = 15, minutes_used = 30),
    ]
    
    df = pd.DataFrame(habits)
    
    print(tabulate(df, headers='keys', tablefmt='psql'))
    
    
if __name__ == '__main__':
    main()