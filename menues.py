from colorama import *
import json
from json import *
from os import system, name




def check_if_exists(username):
    with open('game.json', 'r+') as f:
        name=json.load(f)
        keys=name.keys()
        if username in keys:
            print("TRUE")
        else:
            print("FALSE")
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
    with open('game.json', "r") as data:
        json_data = json.load(data)
        json_data[name] += points
    with open('game.json', "w") as data:
        data.write(dumps(json_data))


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


##########################################
