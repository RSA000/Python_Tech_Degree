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
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Basketball Team Stats Tool \n\n')
    print('== MENU == \n')
    print('Options Index:')
    print('A) Display Teams')
    print('B) Quit \n')
    
    
    while True:
        choice = input("Please enter an option \n")
        if choice.upper() == 'A':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==================')
            print('===== TEAMS ======')
            print('==================')
            for i in range(len(team_list)):
                print(f"{i+1}: ", team_list[i][0])
            print('================== \n\n')
            break
        elif choice.upper() =='B':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("THANK YOU")
            sleep(2)
            sys.exit()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Sorry, thats not a valid input (A or B)")
            continue
    
    
    while True:
        team_choice = input(f"Please enter an option \n {1}-{len(team_list)} - Teams \n type B to quit \n")
        os.system('cls' if os.name == 'nt' else 'clear')

        if team_choice.upper() == 'B':
            print("THANK YOU")
            sleep(1.5)
            sys.exit()
        elif int(team_choice) <= len(team_list):
            chosen_team = team_list[(int(team_choice) -1)]    
            team_name = chosen_team[0].upper()
            heights = [i['height'] for i in chosen_team]
            heights_average = round((sum(heights)/len(chosen_team)),1)
            experienced = 0
            unexperienced = 0

            for i in chosen_team:
                if i['experience'] == True:
                    experienced += 1
                else:
                    unexperienced += 1


            print("=====================")
            print(f'TEAM: {team_name}')
            print("=====================")
            print('Average Height \n'.center(20), f'[{heights_average}]'.center(10))
            print("----------------------")
            print(f' total players {len(chosen_team)}')
            print("----------------------")
            print('Experienced Players \n', f'[{experienced}]'.center(15))
            print("----------------------")
            print('Unexpienced Players \n', f'[{unexperienced}]'.center(15))
            print("----------------------")
            print("=====================")
            print("|||||||||||||||||||||")
            print("=====================")
            print("PLAYERS".center(20))
            print("=====================")
            for i in chosen_team:
                print(i['name'].center(20))            
            print("=====================")
            print("|||||||||||||||||||||")
            print("=====================")
            print("GUARDIANS".center(20))
            print("=====================")
            for i in chosen_team:
                print(i['guardians'].center(20))
            print("===================== \n")
        else:
            print('Thats not a valid options :/ Choose a number to select a team or B to quit')
            continue
        
    
    
        
        
if __name__ == "__main__":
    teams, players = clean_data()
    team_list = balance_teams(teams, players)
    console(team_list)
    
    
    