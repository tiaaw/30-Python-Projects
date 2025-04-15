import random

def sum_dice(rolls: list) -> int:
    sum = 0
    for i in range(len(rolls)):
        sum += rolls[i]
    return sum

def roll_dice(amount:int = 2) ->list[int]:
    if amount <= 0: 
        raise ValueError
    
    rolls = []
    for i in range(amount):
        random_roll = random.randint(1, 6)
        rolls.append(random_roll)
                
    return rolls

def main(): 
    while True: 
        try:
            user_input = input("How many dice would you like to roll? ")
            
            if user_input.lower() == 'exit': 
                print('Thanks for playing!')
                break
            
            rolls = roll_dice(int(user_input))
            
            # Asterix unpacks the values from the list
            print(*rolls, sep=',')
            print(f"The sum of the dice is: {int(sum_dice(rolls))}")
            
        except ValueError: 
            print("(Please enter a valid number)")
            
if __name__ == '__main__':
    main()