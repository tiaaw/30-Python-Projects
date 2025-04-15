from random import choice

def run_game(): 
    word = choice(['apple', 'secret', 'banana'])
    username = input('What is your name?')
    print(f'Welcome to hangman, {username}!')
    
    #Set up
    guessed = ''
    tries = 3 # only have 3 tries
    
    while tries > 0: 
        blanks = 0
        
        print('Word: ', end='')
        for char in word: 
            if char in guessed: 
                print(char, end='')
            else: 
                print('_', end='')
                blanks += 1
                
        print() #   adds a blank line
        
        if blanks == 0: 
            print('You got it!')
            break
        
        guess = input('Enter a letter: ')
        
        if guess in guessed: 
            print(f"You have already guessed: {guess}. Please try another letter.")
            continue
        
        guessed += guess
         
        if guess not in word: 
            tries -= 1
            print('Sorry that was wrong. You have {tries} remaining.')
    
            if tries == 0: 
                print("No more tries remaining. You lose")
                break
            
if __name__ == '__main__':
    run_game()