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
    username = menu.startScreen()
    menu.clear()
    menu.printLogo()
    hero = menu.hero_menu()
    menu.clear()
    menu.printLogo()

    ds = Dungeon(menu.select_map())
    coordinates = ds.start_room
    ds.print_dungeon(coordinates)
    previous_cords = coordinates #Exists only to initiate variable for escape-function
    while True:
        if_escape = True
        menu.clear()
        menu.printLogo()
        
        check_room = check(hero, ds, coordinates)
        
        if check_room[0]:
            if hero.ai == True:
                return_value = menu.ai_attack_menu()
            else:
                return_value = menu.attack_menu()
            x = coordinates[0]
            y = coordinates[1]
            if return_value == "attack":
                if hero.ai == True: #If AI-Flag is True uses AI-Attack without input
                    battle.ai_attack(hero, sort(ds.dungeon[x][y].monsters), username)
                else:
                    battle.attack(hero, sort(ds.dungeon[x][y].monsters), username)
                ds.dungeon[coordinates[0]][coordinates[1]].monsters = [] #Clear monster from Room Object
                ds.dungeon[coordinates[0]][coordinates[1]].marker = '[X]'
            elif return_value == "escape":
                battle.escape(hero, sort(ds.dungeon[x][y].monsters), username)
                ds.move("", previous_cords) #Moves to previous room if escape is Succes
                coordinates = previous_cords #The new cords is the old b/c went back
                if_escape = False

        if check_room[1]:
            if if_escape == True:
                hero.points += coinCount(check_room[1])  # Adds sum of treasures to Hero's attribute   
                print(f"Collected so far: {hero.points}g")
                ds.dungeon[coordinates[0]][coordinates[1]].treasure = [] #Clear treasure from Room Object
                ds.dungeon[coordinates[0]][coordinates[1]].empty = True #For AI to determine if the room is empty or not
                ds.dungeon[coordinates[0]][coordinates[1]].marker = '[X]'
        else:
            print("""
                                            Room is empty""")
            ds.dungeon[coordinates[0]][coordinates[1]].marker = '[X]'
        
        exit_check(hero, ds, coordinates, username) #Checks if Exit flag is True then prompts user for confirmation
        ds.print_dungeon(coordinates)
        if hero.ai == True:
            sleep(3)
            previous_cords = coordinates
            coordinates = ds.ai_move(coordinates)
        else:
            direction = print_move()
            previous_cords = coordinates #Previous Cords
            coordinates = ds.move(direction, coordinates)
        #input()

game()
