import json
from json import *
import os
from time import sleep
import menu
import dungeon_map


#################################################################################################################

# menu to type in name and save/load file
def check_if_exists(username):
    with open('game.json', 'r+') as f:
        
        playerName = json.load(f)
        keys = playerName.keys()
        if username in keys:
            print(f"Welcome back {username}! You have {playerName[username]} points")
            sleep(2.5)
        else:
            print(f"Welcome {username} to Dungeon Run!! Lets begin")
            sleep(2.5)
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
    username = input(
                     """
                                    WELCOME TO DUNGEON RUN!

                                     ENTER PLAYER NAME :""")
    check_if_exists(username)
    # return username
    check_if_exists(username)

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
    menu.printLogo()
    print("""
                                        You've chosen 'Knight'!
    """)
    sleep(1)

def Wizard():
    clear()
    menu.printLogo()
    print("""
                                        You've chosen 'Wizard'!
    """)
    sleep(1)

def Thief():
    clear()
    menu.printLogo()
    print("""
                                        You've chosen 'Thief'!
    """)
    sleep(1)

def Saved():
    print("Select Saved Hero: ")


# menu to select hero
def hero_menu():
    # First menu to select either User or AI as the player
    print("""
                            Start by choosing a User or AI to play:
                                                1. AI
                                                2. User
    \n""")
    choice = input("""   
                                                Select the play method: """)
    if choice == '1':
        # AI will play
        play_AI()
    else:
        # User will play
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


# clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



#############################################################################################################

# menu to select map size
def select_map():
    size = input("""
                                Select size of the map:
                                        1. Small (4x4)
                                        2. Medium (5x5)
                                        3. Large (8x8)

                                        """)
    if size == "1":
        clear()
        menu.printLogo()
        printtestmap(4)
    elif size == "2":
        clear()
        menu.printLogo()
        printtestmap(5)
    elif size == "3":
        clear()
        menu.printLogo()
        printtestmap(8)



def printtestmap(x):
    x = dungeon_map.Dungeon(x)
    x.print_dungeon(0,0)


