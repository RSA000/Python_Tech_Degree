import os

# TODO Create an empty list to maintain the player names
player_names = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
while True:
    if input('Add a player to your team? (yes/no) \n') == 'yes':
        player_names.append(input('please input players name \n'))
        os.system('cls||clear')
        continue
    else:
        os.system('cls||clear')
        print(player_names, '\n')
        print('Total number of players: ', len(player_names), '\n\n')
        for player in range(len(player_names)):
            print(f"player number for {player_names[player]}: ", player+1)
        print('\n\n')
            
        goalkeeper = input('please choose a goalkeeper with the players number')
        print('The goalkeeper is ', player_names[(int(goalkeeper)-1)])
        break
