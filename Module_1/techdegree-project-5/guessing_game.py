import random

from time import sleep
from os import system, name 
# I tried making a flashing screen at the end 
# using this resource https://www.codespeedy.com/clear-screen-in-python/ 


# This section is used to set the the difficulty
low = 1
difficulty = int(input("Please choose your difficulty. 1 is the lowest, 3 is the highest: "))
system('clear')

if difficulty == 1:
    high = 10
elif difficulty == 2:
    high = 100
else:
    high = 250

# I tried to make a title printer so the text would print 
# one letter at a time but it only seems to work when I used it in JupyterLab :/ 

# def title_printer(string):
#     for letter in string:
#         print(letter, end='')
#         sleep(0.5)

# This function is for the ending message
def ending_message(string, exc=5):
    for i in range(exc):
        print(string+('!'*i))
        sleep(0.3)
    system('clear')
    ending_message(string, exc=5)


# This is the actual game function
def start_game(low=0, high=0):
    """ 
    This function takes two parameters (high and low) which determines the 
    range for the guessing game
    """
    answer = random.randint(low, high)
    guess = None
    tries = 0
    
    print(f'Welcome! please choose a number between {low} and {high} \n')
    
    while guess != answer:
        try:
            guess = int(input('Type your guess now: '))
        except ValueError:
            print('You must type a number :p')
            continue
        tries += 1
        if guess > answer:
            print('Too High! Guess again.')
        elif guess < answer:
            print('Too low! Guess again.')
    system('clear')
    
    print(f'Correct! You guessed the number in {tries} tries')


start_game(low,high)

# This runs after the first game is played and allows you to change the difficulty also
if input("Would you like to play again? y/n ") == 'y'.lower():
    difficulty = int(input('Please Choose your difficulty: '))
    start_game(low, high)
else:
    ending_message('Thanks for playing', exc=5)
