from textblob import Textblob
from dataclasses import dataclass


@dataclass
class Mood: 
    emoji: str
    sentiment: float
    

def get_mood(input_text, *, sensitivity) -> Mood:
    polarity = Textblob(input_text).sentiment.polarity
    
    friendly_threshold = sensitivity
    hostile_threshold = -sensitivity
    
    if polarity >= friendly_threshold: 
        return Mood('', polarity)
    elif polarity <= hostile_threshold: 
        return Mood('', polarity)
    else: 
        return Mood('', polarity)
    

def run_bot(): 
    
    print("Bot: Enter some text and I will perform a sentiment analysis on it.")
    while True: 
        user_input = input("You: ")
        mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot: {mood.emoji}, {mood.sentiment}')
        
        
if __name__ == '__main__':
    run_bot()
        