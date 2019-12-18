import menu
from dungeon_map import *
from Heroes import *
from time import sleep


def print_move():
    direction = ""
    f = True
    while f:
        directions = ["w", "a", "s", "d"]
        direction = input("""
                                    CHOOSE DIRECTION TO GO
                                            Up - W
                                            Left - A
                                            Down - S
                                            Right - D

                                            --->""")
        
        if direction.lower() not in directions:
            print("You have to type W, A, S or D")

        else:
            f = False
    
    return direction.lower()

def game():
    menu.printLogo()
    menu.startScreen()
    menu.clear()
    menu.printLogo()
    hero = menu.hero_menu()
    menu.clear()
    menu.printLogo()

    ds = Dungeon(menu.select_map())
    coordinates = ds.start_room
    ds.print_dungeon(coordinates)
    while True:
        menu.clear()
        menu.printLogo()
        ds.print_dungeon(coordinates)
        direction = print_move()
        coordinates = ds.move(direction, coordinates)
        check(hero, ds, coordinates)
        input()

game()
