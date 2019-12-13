import menu
import pickhero
import color
import map
import header
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#header.printLogo()
def select_map():
    size = input("""
                                Select size of the map:
                                        1. Small (4x4)
                                        2. Medium (5x5)
                                        3. Large (8x8)

                                        """)
    if size == "1":
        clear()
        header.printLogo()
        printtestmap(4)
    elif size == "2":
        clear()
        header.printLogo()
        printtestmap(5)
    elif size == "3":
        clear()
        header.printLogo()
        printtestmap(8)



def printtestmap(x):
    x = map.Dungeon(x)
    x.print_dungeon(0,0)

def game():
    header.printLogo()
    menu.startScreen()
    clear()
    header.printLogo()
    pickhero.main_hero()
    clear()
    header.printLogo()
    select_map()
    
temp = 0 
#game()
#print(sys.path)
#x = map.Dungeon(8)
#print(x.dungeon)
#x.print_dungeon(0,1)