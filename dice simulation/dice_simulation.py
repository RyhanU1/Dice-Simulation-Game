import random

def dice_roll():
    
    while True:

        roll = (input("Type 'yes' if you'd like to roll the dice, or 'no' to quit: "))
        lower_roll = roll.lower()

        if lower_roll == 'yes':
            dice = random.randint(1, 6)
            print('You rolled:', dice)

        elif lower_roll == 'no':
            print('Maybe next time!')
            break
        
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

dice_roll()