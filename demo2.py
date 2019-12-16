import menu
import dungeon_map
import os


def game():
    menu.printLogo()
    menu.startScreen()
    menu.clear()
    menu.printLogo()
    menu.hero_menu()
    menu.clear()
    menu.printLogo()
    menu.select_map()
    

game()
