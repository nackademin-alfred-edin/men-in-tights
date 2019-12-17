from colorama import *
import json
from os import system, name



def check_if_exists(username):
    with open('game.json', 'r+') as f:
        name = json.load(f)
        keys = name.keys()
        if username in keys:
            print(f"You have {username}")
        else:
            add_to_file(username)




def add_to_file(username):

    with open('game.json', "r") as f:
        players=json.load(f)
        new_user = {username: 0}
        players.update(new_user)
    with open('game.json', "w") as f:
        json.dump(players, f)
        f.close()


def add_points(name, points):
    with open('game.json', "r") as f:
        json_data = json.load(f)
        json_data[name] += points
    with open('game.json', "w") as f:
        json.dump(json_data, f)
        f.close()

def printLogo():
    print(Fore.RED +
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


def startScreen():
    username = input(Fore.YELLOW +
                     """
                                    WELCOME TO DUNGEON RUN!
                                    
                                    
                                    ENTER PLAYER NAME :""")
    return username


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def print_move():
    print("CHOOSE DIRECTION TO GO")
    print("North- N")
    print("West- W")
    print("East- E")
    print("South- S")
    direction = ""
    f = True
    while f:
        directions = ["n", "w", "e", "s"]
        direction = input("--->")
        
        if direction.lower() not in directions:
            print("You have to tape N,W,E or S")

        else:
            f = False
    
    return direction.lower()



    
