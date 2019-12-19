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
        if_escape = True
        menu.clear()
        menu.printLogo()
        
        check_room = check(hero, ds, coordinates)
        
        if check_room[0]:
            return_value = menu.attack_menu()
            x = coordinates[0]
            y = coordinates[1]
            if return_value == "attack":
                battle.attack(hero, sort(ds.dungeon[x][y].monsters))
                ds.dungeon[coordinates[0]][coordinates[1]].monsters = [] #Clear monster from Room Object
                ds.dungeon[coordinates[0]][coordinates[1]].marker = '[X]'
            elif return_value == "escape":
                battle.escape(hero, sort(ds.dungeon[x][y].monsters))
                if_escape = False

        if check_room[1]:
            if if_escape == True:
                hero.points += coinCount(check_room[1])  # Adds sum of treasures to Hero's attribute   
                print(f"Collected so far: {hero.points}g")
                ds.dungeon[coordinates[0]][coordinates[1]].treasure = [] #Clear treasure from Room Object
                ds.dungeon[coordinates[0]][coordinates[1]].marker = '[X]'
        else:
            print("""
                                            Room is empty""")
            ds.dungeon[coordinates[0]][coordinates[1]].marker = '[X]'

        ds.print_dungeon(coordinates)
        direction = print_move()
        coordinates = ds.move(direction, coordinates)
        #input()

game()
