#from men-in-tights import menu
from menu import *
import menu
import dungeon_map
from dungeon_map import *
import os


def game():

    menu.printLogo()
    menu.startScreen()
    menu.select_map()

if __name__ == "__main__":
    game()

