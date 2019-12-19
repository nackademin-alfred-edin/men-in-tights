from random import randint
import monster_treasure as mt
import color as c
import menues as m
from time import sleep
 

class Dungeon:
    def __init__(self, map_size):
        self.map_size = map_size
        self.start_room = self.start_point()
        self.dungeon = self.generate_map()
        self.generate_exit()
        

    def start_point(self):
        corner = input("""
                                        Where do you want to start?
                                            1. North west
                                            2. North east
                                            3. South west
                                            4. South east
    """)
        if corner == "1":
            return (0, 0)
        elif corner == "2":
            return (0, self.map_size-1)
        elif corner == "3":
            return (self.map_size-1, 0)
        elif corner == "4":
            return (self.map_size-1, self.map_size -1)

    def generate_exit(self):
        exit_list = [(0, 0), (0, self.map_size-1), (self.map_size-1, 0), (self.map_size-1, self.map_size-1)]
        for i in exit_list:
            if self.start_room == i:
                x = self.start_room[0]
                y = self.start_room[1]
                self.dungeon[x][y].exit = True
                exit_list.remove(i)
        index = randint(0, 2)
        x = exit_list[index][0]
        y = exit_list[index][1]
        self.dungeon[x][y].exit = True


    def generate_map(self):
        dungeon = [[] for i in range(self.map_size)]
        for i in range(self.map_size):
            for j in range(self.map_size):
                if self.start_room != (i, j):
                    room = Room(i, j)
                    dungeon[i].append(room)
                else:
                    room = Room(i ,j)
                    room.monsters = []
                    dungeon[i].append(room)
                    
        return dungeon

    

        

#This function print dungeon for user
    def print_dungeon(self, coordinates):
        x = coordinates[0]
        y = coordinates[1]
        for i in range(self.map_size):
            for j in range(self.map_size):
                v = ""
                if j == self.map_size - 1:
                    v = "\n"
                if i == x and j == y:
                    print("[O]", end=v)
                else:
                    print(self.dungeon[i][j].marker, end=v)
    

    def move(self, direction, coordinates): # Hero can go outside the grid. No exception
        x = coordinates[0]
        y = coordinates[1]
        if direction.lower() == "n":
            x -= 1
        elif direction.lower() == "w":
            y -= 1
        elif direction.lower() == "e":
            y += 1
        elif direction.lower() == "s":
            x += 1
        return (x, y)


    def check_move(self, x, y): #check room if it was looted
        if self.dungeon[x][y].empty == False:
            return False
        else:
            return True


    def ai_move(self, coordinates):#ai have to choose room that wasn't looted
        wrong_move = True
        count = 3
        while wrong_move:
            x = coordinates[0]
            y = coordinates[1]
            north = x - 1
            west = y - 1
            east = y + 1
            south = x + 1
            if x == 0 and y == 0:
                functions = [east, south]
                index = randint(0, 1)
                if index == 1:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1
            elif x == 0 and y < self.map_size-1:
                functions = [west, east, south]
                index = randint(0,2)
                if index == 2:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1 
            elif x == 0 and y == self.map_size-1:
                functions = [ west, south]
                index = randint(0,1)
                if index == 1:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1
            elif x < self.map_size-1 and y == self.map_size-1:
                functions = [north, west, south]
                index = randint(0,2)
                if index == 0 or index == 2:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1             
            elif x == self.map_size-1 and y == self.map_size-1:
                functions = [north, west]
                index = randint(0,1)
                if index == 0:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1
            elif x == self.map_size-1 and y < self.map_size-1:
                functions = [north, east]
                index = randint(0,1)
                if index == 0:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1
            elif x == self.map_size-1 and y == 0:
                functions = [north, east]
                index = randint(0,1)
                if index == 0:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1
            elif x < self.map_size-1 and y == 0:
                functions = [north, east, south]
                index = randint(0,2)
                if index == 0 or index == 2:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1
            else:
                functions = [north, west, east, south]
                index = randint(0,3)
                if index == 0 or index == 3:
                    x = functions[index]
                else:
                    y = functions[index]
                wrong_move = self.check_move(x, y)
                count -= 1
            if count == 0:
                break
        return (x, y)

                

#Object Room selfgenerate monsters and treasures 
class Room:
    def __init__(self, x, y):
        self.coordinates =(x, y)
        self.marker = "[ ]"
        self.monsters = []
        self.treasure = []
        self.empty = False
        self.exit = False
        self.place_content()

    def place_content(self):
        possible_monsters = ["spider", "skeleton", "orc", "troll"]
        possible_treasure = ["coins", "pouch", "jewelry", "gemstone", "chest"]
        for i in possible_monsters:
            if i == "spider":
                if mt.Spider.commonness >= randint(0, 100):
                    spider = mt.Spider()
                    self.monsters.append(spider)
            if i == "skeleton":
                if mt.Skeleton.commonness >= randint(0, 100):
                    skeleton = mt.Skeleton()
                    self.monsters.append(skeleton)
            if i == "orc":
                if mt.Orc.commonness >= randint(0, 100):
                    orc = mt.Orc()
                    self.monsters.append(orc)
            if i == "troll":
                if mt.Troll.commonness >= randint(0, 100):
                    troll = mt.Troll()
                    self.monsters.append(troll)
        for i in possible_treasure:
            if i == "coins":
                if mt.Coins.commonness >= randint(0, 100):
                    coins = mt.Coins()
                    self.treasure.append(coins)
            if i == "pouch":
                if mt.Pouch.commonness >= randint(0, 100):
                    pouch = mt.Pouch()
                    self.treasure.append(pouch)
            if i == "jewelry":
                if mt.Jewelry.commonness >= randint(0, 100):
                    jewelry = mt.Jewelry()
                    self.treasure.append(jewelry)
            if i == "gemstone":
                if mt.Gemstone.commonness >= randint(0, 100):
                    gemstone = mt.Gemstone()
                    self.treasure.append(gemstone)
            if i == "chest":
                if mt.Chest.commonness >= randint(0, 100):
                    chest = mt.Chest()
                    self.treasure.append(chest)


ds = Dungeon(4)
coordinates = ds.start_room
ds.print_dungeon(coordinates)
print(ds.dungeon[0][0].exit)
print(ds.dungeon[0][3].exit)
print(ds.dungeon[3][3].exit)
print(ds.dungeon[3][0].exit)