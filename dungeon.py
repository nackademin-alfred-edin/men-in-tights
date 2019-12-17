from random import randint
import monster_treasure as mt
import color as c
import menues
 

class Dungeon:
    def __init__(self, map_size, x, y):
        self.map_size = map_size
        self.start_room = self.start_point(x, y)
        self.dungeon = self.generate_map()
        self.generate_exit()
        

    def start_point(self, x, y):
        return (x, y)

    def generate_exit(self):
        pass


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
    def print_dungeon(self, x, y):
        for i in range(self.map_size):
            for j in range(self.map_size):
                v = ""
                if j == self.map_size - 1:
                    v = "\n"
                if i == x and j == y:
                    print(c.color.fg.orange, "[O]", end=v)
                else:
                    print(c.color.fg.purple, self.dungeon[i][j].marker, end=v + c.color.fg.reset)
    

    def move(self, direction, x, y): # Hero can go outside the grid. No exeption
        if direction.lower() == "n":
            x -= 1
        elif direction.lower() == "w":
            y -= 1
        elif direction.lower() == "e":
            y += 1
        elif direction.lower() == "s":
            x += 1

        return x, y

#Object Room selfgenerate monsters and treasures 
class Room:
    def __init__(self, x, y):
        self.coordinates =(x, y)
        self.marker = "[ ]"
        self.monsters = []
        self.treasure = []
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


