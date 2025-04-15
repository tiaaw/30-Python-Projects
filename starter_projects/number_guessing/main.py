from random import randint

lower_num, higher_num = 1, 10

# Generate a number between 1-10, 10 inclusive
random_number = randint(lower_num, higher_num)

print(f"Guess the number in the range from {lower_num} to {higher_num}.")

while True: 
    try: 
        user_guess = int(input('Guess: '))
    except ValueError: 
        print("Please enter a valid number")
        continue
        
    if user_guess > random_number: 
        print('The number is lower.')
    elif user_guess < random_number: 
        print('The number is higher.')
    else:
        print('You guessed it!')
        break 