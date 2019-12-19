import json
import os
from time import sleep
import dungeon_map
import Heroes
import battle


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
    printLogo()
    
    hero = Heroes.Knight()
    print("""
                                        You've chosen 'Knight'!
                                                               .-.
                                                              {{#}}
                                              {}               8@8
                                            .::::.             888
                                        @\\/W\/\/W\//@         8@8
                                         \\/^\/\/^\//     _    )8(    _
                                          \_O_{}_O_/     (@)__/8@8\__(@)
                                     ____________________ `~"-=):(=-"~`
                                    |<><><>  |  |  <><><>|     |.|
                                    |<>      |  |      <>|     |S|
                                    |<>      |  |      <>|     |'|
                                    |<>   .--------.   <>|     |.|
                                    |     |   ()   |     |     |P|
                                    |_____| (O\/O) |_____|     |'|
                                    |     \   /\   /     |     |.|
                                    |------\  \/  /------|     |U|
                                    |       '.__.'       |     |'|
                                    |        |  |        |     |.|
                                    :        |  |        :     |N|
                                     \       |  |       /      |'|
                                      \<>    |  |    <>/       |.|
                                       \<>   |  |   <>/        |K|
                                        `\<> |  | <>/'         |'|
                                          `-.|__|.-`           \ /
                                                                ^
    """)
    sleep(2)
    return hero

def Wizard():
    clear()
    printLogo()
    hero = Heroes.Wizard()
    print("""
                                        You've chosen 'Wizard'!
                                                    ,---.
                                                   /    |
                                                  /     |
                                                 /      |
                                                /   W   |
                                           ___,'        |
                                         <  -'          :   >
                                         `-.__..--'``-,_\_.-`
                                             |o/ ` o,.)_`>
                                             :/ `     ||/)
                                             (_.).__,-` |\ 
                                             /( `.``   `| :
                                             \'`-.)  `  ; ;
                                             | `       /-<
                                             |     `  /   `.
                            ,-_-..____      /|  `    :__..-'\   
                            /,'-.__\\  ``-./ :`      ;       \ 
                            `\ `\  `\\  \ :  (   `  /  ,   `. \ 
    """)
    sleep(2)
    return hero

def Thief():
    clear()
    printLogo()
    hero = Heroes.Thief()
    print("""
                                        You've chosen 'Thief'!
                                              _..__
                                            .'  I  '.
                                            |.-"'"-.|
                                           _;.-"'"-.;_
                                       _.-' _..-.-.._ '-._
                                      ';--.-(_o_I_o_)-.--;'
                                     `. | |  | |  | | .`
                                         `-\|  | |  |/-'
                                            |  | |  |
                                            |  \_/  |
                                         _.'; ._._. ;'._
                                    _.-'`; | \  -  / | ;'-.
                                 .' :  /  |  |   |  |  \  '.
                                /   : /__ \  \___/  / __\ : `.
                               /    |   /  '._/_\_.'  \   :   `\ 
                              /     .  `---;""''"'-----`  .     \ 
                             /      |      |()    ()      |      \ 
                            /      /|      |              |\      \ 
                           /      / |      |()    ()      | \      \ 
    """)
    sleep(2)
    return hero



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
        return choice_menu[choice]()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



#############################################################################################################

# menu to select map size
def small():
    return 4

def medium():
    return 5

def large():
    return 8

def select_map():
    size = input("""
                                        Select size of the map:
                                            1. Small (4x4)
                                            2. Medium (5x5)
                                            3. Large (8x8)

                                            --->""")
    choice_menu = { '1': small(),
                    '2': medium(),
                    '3': large()}
    if size not in choice_menu.keys():
        clear()
        printLogo()
        print("Please pick a number")
        sleep(0.5)
        size = 0
        select_map()
    else:
        return choice_menu[size]
    

########################################################################################################################

def attack_menu():

    choice = input("""
                                               \|||/
                                               (o o)
--------------------------------------------ooO-(_)-Ooo-----------------------------------------
                        A monster is lurking in this room, do you fight or flight!?
                                            1. Attack
                                            2. Escape
                                            
                                            --->""")
    choice_menu = { '1': "attack",
                    '2': "escape"
                    }
    if choice not in choice_menu.keys():
        print("""
                                        Please type in 1 or 2
        """)
    else:
        if choice_menu[choice] == "attack":
            return "attack"#battle.attack(hero, sort(ds.dungeon[x][y].monsters))
        elif choice_menu[choice] == "escape":
            return "escape"#battle.escape(hero, sort(ds.dungeon[x][y].monsters))


##################################################################################################################

def roll_dice():
    print("""
                                           .-------.    ______
                                          /   o   /|   /\     \  
                                         /_______/o|  /o \  o  \ 
                                         | o     | | /   o\_____\ 
                                         |   o   |o/ \o   /o    /
                                         |     o |/   \ o/  o  /
                                         '-------'     \/____o/
                                                
                                                Rolling...""")    