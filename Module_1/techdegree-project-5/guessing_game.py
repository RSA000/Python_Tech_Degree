import random
import os

from time import sleep

# I tried making a flashing screen at the end 
# using this resource https://www.codespeedy.com/clear-screen-in-python/ 

# this is for the ending message. 
def ending_message(string, exc=5):
    """
    This function takes a string as an input prints to screen with
    increasing exclamations (the amount of following exclamations can be
    change but increasing/descreasing exc)
    """
    for i in range(exc):
        print(string+('!'*i))
        sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
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
    global highscore
    
    print(f'Welcome! please choose a number between {low} and {high} \n')
    print('==================')
    print('HIGHSCORE')
    print('==',highscore,'==')
    print('==================')
    
    
    while guess != answer:
        try:
            guess = int(input('Type your guess now: '))
        except ValueError:
            print('You must type a number :p')
            continue
        tries += 1
        if guess > answer and guess > high:
            print('Way too high. number out of guessing range \n')  
        elif guess > answer:
            print('Too High! Guess again \n.')
        elif guess < answer and guess < low:
            print('Way too low! number out of guessing range \n')
        elif guess < answer:
            print('Too low! Guess again. \n')
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f'Correct! You guessed the number in {tries} tries')
    if highscore > tries:
        print('New highscore!')
        highscore = tries

    # This runs after the first game is played and allows you to change the difficulty also
    if input("Would you like to play again? y/n ") == 'y'.lower(): 
        while True:
            difficulty = input('Please Choose your difficulty: ')
            if difficulty == '1':
                high = 10
                break
            elif difficulty == '2':
                high = 100
                break
            elif difficulty == '3':
                high = 250
                break
            else:
                print('Sorry thats not a valid input :( ')
            continue
        start_game(low, high)
    else:
        ending_message('Thanks for playing', exc=5)


# This section is used to set the the difficulty
highscore = 1000
low = 1
while True:
    difficulty = input("Please choose your difficulty. 1 is the lowest, 3 is the highest: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if difficulty == '1':
        high = 10
        break
    elif difficulty == '2':
        high = 100
        break
    elif difficulty == '3':
        high = 250
        break
    else:
        print("Oh no! Thats not a valid input D: ")
        continue

    
start_game(low,high)