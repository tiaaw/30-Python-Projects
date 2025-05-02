from Flask import Flask, request 
from random import randint, choice
from datetime import datetime 

app = Flask(__name__)

@app.route('/') # endpoint for the root URL/homepage
def index(): 
    phrases = ['Welcome to this page!', 'You are looking good today!', 'The weather is great!']
    return {'phrase': choice(phrases), 
            'date': datetime.now()} # return a random phrase from the list
    

@app.route('/random') # endpoint for the random URL
def random(): 
    number_input = request.args.get('number', type=int, default = 100) 
    text_input = request.args.get('text', type=str, default = '')
    
    if isinstance(number_input, int):
        return {
            'input': number_input,
            'random': randint(0, number_input), 
            'text': text_input, 
            'date': datetime.now()
        }
        
    else: 
        return {'Error': 'Please only use numbers in the input',}
    
    
if __name__ == '__main__':
    app.run()