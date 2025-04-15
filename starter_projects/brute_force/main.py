import itertools #in built module for iterables and looking through them and efficiently
import string 
import time 

def common_guess(word):
    with open('brute_force/words.txt', 'r') as words: 
        word_list = words.read().splitlines()
        
        for i, match in enumerate(word_list, start=1):
            if match == word: 
                return f'Common match: {match} (#{i})'
            
            
def brute_force(word, length, digits = False, symbols = False) -> str | None: 
    chars = string.ascii_lowercase
    
    if digits: 
        chars += string.digits
    
    if symbols: 
        chars += string.punctuation
        
    attempts = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess = ''.join(guess)
        
        if guess == word: 
            return f'"{word}" was cracked in {attempts:,} guesses.'
        
        print(guess, attempts)
    return None
            
if __name__ == '__main__':
    print('searching...')
    password = 'abc1'
    
    start_time = time.perf_counter()
    
    # Walrus operator 
    # common_match is assigned the value of common_guess 
    # if None it won't execute
    # else it executes and common_guess only returns None or str
    if common_match := common_guess(password): 
        print(common_match)
    else: 
        if cracked := brute_force(password, length = 4, digits=True, symbols=True):
            print(cracked)
        else:
            print('There was no match...')
            
    end_time = time.perf_counter()
    print(round(end_time - start_time, 2), 's')