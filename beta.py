import menu
import dungeon_map


def print_move():
    direction = ""
    f = True
    while f:
        directions = ["n", "w", "e", "s"]
        direction = input("""
                                    CHOOSE DIRECTION TO GO
                                            North- N
                                            West- W
                                            East- E
                                            South- S

                                            --->""")
        
        if direction.lower() not in directions:
            print("You have to tape N,W,E or S")

        else:
            f = False
    
    return direction.lower()

def game():
    menu.printLogo()
    menu.startScreen()
    menu.clear()
    menu.printLogo()
    menu.hero_menu()
    menu.clear()
    menu.printLogo()

    ds = dungeon_map.Dungeon(menu.select_map())
    coordinates = ds.start_room
    ds.print_dungeon(coordinates)
    while True:
        menu.clear()
        menu.printLogo()
        ds.print_dungeon(coordinates)
        direction = print_move()
        coordinates = ds.move(direction, coordinates)
        


game()
