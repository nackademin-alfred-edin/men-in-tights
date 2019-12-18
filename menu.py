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
            clear()
            printLogo()
            print(f"""
                                Welcome back {username}! You have {playerName[username]} points""")
            sleep(2)  
        else:
            clear()
            printLogo()
            print(f"""
                                Welcome {username} to Dungeon Run!! Lets begin""")
            sleep(2)
            add_to_file(username)


def add_to_file(username):
    with open('game.json', "r") as f:
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

                                       Enter username:""")
    check_if_exists(username)
    return username


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    user = startScreen()
    check_if_exists(username=user)

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
    sleep(2)

def Wizard():
    clear()
    menu.printLogo()
    print("""
                                        You've chosen 'Wizard'!
    """)
    sleep(2)

def Thief():
    clear()
    menu.printLogo()
    print("""
                                        You've chosen 'Thief'!
    """)
    sleep(2)

def Saved():
    print("Select Saved Hero: ")


def AI_Knight():
    clear()
    printLogo()
    print("""
                                        AI have chosen 'AI Knight'!
        """)
    sleep(2)

def AI_Wizard():
    clear()
    printLogo()
    print("""
                                        AI have chosen 'AI Wizard'!
            """)
    sleep(2)


def AI_Thief():
    clear()
    printLogo()
    print("""
                                        AI have chosen 'AI Thief'!
            """)
    sleep(2)


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


# menu to select hero
def hero_menu():
    print("""
                                    Start by choosing your hero
                                            1. Knight
                                            2. Wizard
                                            3. Thief

                                Or load an AI to play the game for you!
                                            4. AI Knight
                                            5. AI Wizard
                                            6. AI Thief    
""")
    choice = input("""   
                                            ---> """)
    choice_menu =  {'1': Knight,
                    '2': Wizard,
                    '3': Thief,
                    '4': AI_Knight,
                    '5': AI_Wizard,
                    '6': AI_Thief}
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

                                            --->""")
    if size == "1":
        return 4
    elif size == "2":
        return 5
    elif size == "3":
        return 8