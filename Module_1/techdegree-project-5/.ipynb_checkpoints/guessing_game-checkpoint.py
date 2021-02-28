import random


low = 0
difficulty = int(input("Please choose your difficulty. 1 is the lowest, 3 is the highest: "))

if difficulty == 1:
    high = 10
elif difficulty == 2:
    high = 100
else:
    high = 250



def start_game(low=0, high=0):
    answer = random.randint(low, high)
    guess = 0
    tries = 0
    
    print(f'Welcome! please choose a number between {low} and {high}')

    while guess != answer:
        guess = int(input('Type your guess now: '))
        tries += 1
        if guess > answer:
            print('To High! Guess again.')
        elif guess < answer:
            print('To low! Guess again.')
    print(f'Correct! You guessed the number in {tries} tries')


start_game(low,high)

if input("Would you like to play again? y/n ") == 'y'.lower():
    difficulty = int(input('Please Choose your difficulty: '))
    start_game(low, high)