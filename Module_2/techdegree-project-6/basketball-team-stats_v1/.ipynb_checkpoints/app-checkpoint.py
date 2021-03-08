import constants
import copy
import os
import pprint
import random
import statistics
import sys
from time import sleep

def clean_data():
    """
    This function creates a copy of TEAMS and PLAYERS from constants.py and
    changes the height values to a float data type and the experience values to 
    a boolean data type. 
    """
    teams = copy.deepcopy(constants.TEAMS)
    players = copy.deepcopy(constants.PLAYERS)
    
    for player in players:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    for player in players:
        player['height'] = float(player['height'][0:2])
        
    for player in players:
        player['guardians'] = player['guardians'].split(' and ')
        
    return teams, players
    
        


def balance_teams(teams, players):
    """
    This function creates two lists from the copied PLAYERS list, experienced and unexperienced.
    Experienced and unexperienced are shuffled so the teams change each time the program runs.
    
    A list of lists is created called 'team_list' where the number of lists in 'team_list' depends on
    the number of teams in TEAMS.
    
    Each list in 'team_list' is appended a player from the experienced and unexperienced list.
    The appended players are removed from the lists and loops until the list is exhausted. 
    """
    players_per_team = len(players) / len(teams)    
    experienced = []
    unexperienced = []
    
    for player in players:
        if player['experience'] == True:
            experienced.append(player)
        else:
            unexperienced.append(player)
    random.shuffle(experienced)
    random.shuffle(unexperienced)
    
    team_list = [[team] for team in teams]
    
    for i in range(len(team_list)):
        for j in range(int(players_per_team/2)):
            team_list[i].append(experienced.pop())
            team_list[i].append(unexperienced.pop())
    return team_list

            
def console(team_list):
    """This function will display team stats."""
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===========================")
    print('Basketball Team Stats Tool\n===========================\n\n')
    print('== MENU == \n')
    print('Options Index:')
    print('A) Display Teams')
    print('B) Quit \n')
    
    
    while True:
        choice = input("Please enter an option \n")
        if choice.upper() == 'A':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice.upper() =='B':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thank You")
            sleep(2)
            sys.exit()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Sorry, thats not a valid input (A or B)")
            continue
    
    while True:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==================')
            print('===== TEAMS ======')
            print('==================')
            for i in range(len(team_list)):
                print(f"{i+1}: ", team_list[i][0])
            print('================== \n\n')
            team_choice = (input(f"Please select a team (1-{len(team_list)}) \n Or press B to quit ")) 
            try:
                int(team_choice) in [i for i in range(len(team_list)+1)]
                if int(team_choice) > len(team_list):
                    print(f'Sorry that is not a valid input. Please type a number between (0-{len(team_list)}) or B to quit')
                    sleep(0.9)
                    continue
                team_choice = int(team_choice) -1
                break
            except ValueError:
                if team_choice.upper() == 'B':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Thank You")
                    sleep(2)
                    sys.exit()
                else:
                    print(f'Sorry that is not a valid input. Please type a number between (0-{len(team_list)}) or B to quit')
                    sleep(0.9)

        team_name = team_list[team_choice][0]
        total_players = len(team_list[team_choice][1:])
        player_names = [player['name'] for player in team_list[team_choice][1:]]
        guardian_names = [player['guardians'] for player in team_list[team_choice][1:]]
        player_heights = [player['height'] for player in team_list[team_choice][1:]]
        height_average = round(sum(player_heights) / len(player_heights), 1)

        experienced = 0
        unexperienced = 0
        for i in range(len(team_list[team_choice][1:])):
            if team_list[team_choice][1:][i]['experience'] == True:
                experienced += 1
            else:
                unexperienced += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=======================")
        print(f"==== {team_name.upper()} ====".center(22))
        print("=======================")
        print("|||||||||||||||||||||||")
        print("________________________")
        print(f"Total Players: {total_players}")
        print("________________________")
        print(f"Experienced Players {experienced}")
        print(f"Unexpienced Players {unexperienced}")
        print("________________________")
        print(f"Average Height {height_average}")
        print("=======================")
        print("Player Names: \n")
        for name in player_names:
            print(name, end=', ')
        
        print("\n=======================")
        print("Guardian Names:\n")
        for guardian in guardian_names:
            for i in guardian:
                print(i, end=(', '))
        print("\n=======================")
        
        while True:
            end_message = input("Choose another team? y/n \n")
            if end_message.upper() == 'Y':
                break
            elif end_message.upper() == 'N':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Thank You")
                    sleep(2)
                    sys.exit()
            else:
                print("Sorry that is not a valid input, please type Y or N")
                sleep(0.9)
                os.system('cls' if os.name == 'nt' else 'clear')
                
        continue
    
if __name__ == "__main__":
    teams, players = clean_data()
    team_list = balance_teams(teams, players)
    console(team_list)
    
    
    