import json
from json import *
import os
from time import sleep
import dungeon_map


#################################################################################################################

# menu to type in name and save/load file
def check_if_exists(username):
    with open('game.json', 'r+') as f:
        
        playerName = json.load(f)
        keys = playerName.keys()
        if username in keys:
            print(f"Welcome back {username}! You have {playerName[username]} points")
            sleep(1.5)
        else:
            print(f"Welcome {username} to Dungeon Run!! Lets begin")
            sleep(1.5)
            add_to_file(username)


def add_to_file(username):
    with open('game.json', "r") as f:
        players={}
        players = json.load(f)
        new_user = {username: 0}
        players.update(new_user)
    with open('game.json', "w") as f:
        json.dump(players, f)
        f.close()


def add_points(name, points):
    with open('game.json', "r") as data:
        json_data = json.load(data)
        json_data[name] += points
    with open('game.json', "w") as data:
        data.write(dumps(json_data))


def startScreen():
    # First menu to select either User or AI as the player
    choice = input(
                     """
                                    WELCOME TO DUNGEON RUN!
                                    
                            Start by choosing a User or AI to play:
                                            1. AI
                                            2. User
                                            
                            Please enter play method: """)
    choice_menu = {'1': AI_choice_menu,
                   '2': user_choice_menu}
    if choice not in choice_menu.keys():
        print("Please enter either 1 or 2 to continue.")
    else:
        choice_menu[choice]()


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    startScreen()
    # user = startScreen()
    # check_if_exists(username=user)

#################################################################################################################

# DUNGEON RUN header
def printLogo():
    print(
        """
@@@@@@@   @@@  @@@  @@@  @@@   @@@@@@@@  @@@@@@@@   @@@@@@   @@@  @@@     @@@@@@@   @@@  @@@  @@@  @@@  
@@@@@@@@  @@@  @@@  @@@@ @@@  @@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@ @@@     @@@@@@@@  @@@  @@@  @@@@ @@@  
@@!  @@@  @@!  @@@  @@!@!@@@  !@@        @@!       @@!  @@@  @@!@!@@@     @@!  @@@  @@!  @@@  @@!@!@@@  
@!@  @!@  !@!  @!@  !@!!@!@!  !@!        !@!       !@!  @!@  !@!!@!@!     !@!  @!@  !@!  @!@  !@!!@!@!  
!@!  !@!  @!@  !@!  @!@ !!@!  !@! @!@!@  @!!!:!    @!@  !@!  @!@ !!@!     @!@!!@!   @!@  !@!  @!@ !!@!  
!@!  !!!  !@!  !!!  !@!  !!!  !!! !!@!!  !!!!!:    !@!  !!!  !@!  !!!     !!@!@!    !@!  !!!  !@!  !!!  
!!:  !!!  !!:  !!!  !!:  !!!  :!!   !!:  !!:       !!:  !!!  !!:  !!!     !!: :!!   !!:  !!!  !!:  !!!  
:!:  !:!  :!:  !:!  :!:  !:!  :!:   !::  :!:       :!:  !:!  :!:  !:!     :!:  !:!  :!:  !:!  :!:  !:!  
:::: ::   ::::: ::  ::   ::   ::: ::::   :: ::::   ::::: ::   ::   ::     ::   :::  ::::: ::  ::    ::  
:: :  :    : :  :   ::    :    :: :: :   : :: ::    : :  :    ::    :     :    : :   : :  :   ::    :   
""")


##############################################################################################################


def Knight():
    clear()
    printLogo()
    print("""
                                        You've chosen 'Knight'!
    """)
    sleep(1)

def Wizard():
    clear()
    printLogo()
    print("""
                                        You've chosen 'Wizard'!
    """)
    sleep(1)

def Thief():
    clear()
    printLogo()
    print("""
                                        You've chosen 'Thief'!
    """)
    sleep(1)

def Saved():
    print("Select Saved Hero: ")

def user_choice_menu():
    username = input(
        """
                                ENTER PLAYER NAME: """)
    check_if_exists(username)

    print("""
                    Start by choosing your hero, or load a previous saved hero
                                            1. Knight
                                            2. Wizard
                                            3. Thief
                                            4. Load Saved Hero
    \n""")
    choice = input("""   
                                Enter number for Hero: """)
    choice_menu =  {'1': Knight,
                    '2': Wizard,
                    '3': Thief,
                    '4': Saved}
    if choice not in choice_menu.keys():
        print("Please choose a hero ")
    else:
        choice_menu[choice]()

def AI_Knight():
    clear()
    printLogo()
    print("""
                                            AI have chosen 'AI Knight'!
        """)
    sleep(1)

def AI_Wizard():
    clear()
    printLogo()
    print("""
                                            AI have chosen 'AI Wizard'!
            """)
    sleep(1)


def AI_Thief():
    clear()
    printLogo()
    print("""
                                            AI have chosen 'AI Thief'!
            """)
    sleep(1)


def AI_choice_menu():
    print("""
                            Start by choosing your AI hero:
                                                1. AI Knight
                                                2. AI Wizard
                                                3. AI Thief
    \n""")
    choice = input("""   
                                        Enter number for AI Hero: """)
    choice_menu =  {'1': AI_Knight,
                    '2': AI_Wizard,
                    '3': AI_Thief}
    if choice not in choice_menu.keys():
        print("Please choose a hero ")
    else:
        choice_menu[choice]()

# clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#############################################################################################################

# menu to select map size
def select_map():
    size = input("""
                                    Size of the map:
                                        1. Small (4x4)
                                        2. Medium (5x5)
                                        3. Large (8x8)
                                        
                                   Enter map size: """)
    choice_map = {'1': 4,
                  '2': 5,
                  '3': 8}
    if size not in choice_map.keys():
        print("Please choose a defined map size")
    else:
        clear()
        printLogo()
        printtestmap(choice_map[size])

def printtestmap(x):
    x = dungeon_map.Dungeon(x)
    x.print_dungeon(0,0)


