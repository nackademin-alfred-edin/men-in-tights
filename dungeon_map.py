import menu
from random import randint
import monster_treasure as mt
import Heroes
import battle
import die


class Dungeon:
    def __init__(self, map_size):
        self.map_size = map_size
        self.start_room = self.start_point()
        self.dungeon = self.generate_map()
        self.generate_exit()

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
                    room = Room(i, j)
                    room.monsters = []
                    dungeon[i].append(room)

        return dungeon

    def start_point(self):
        menu.clear()
        menu.printLogo()
        corner = input("""
                                        Where do you want to start?
                                            1. North west
                                            2. North east
                                            3. South west
                                            4. South east
                                            
                                            --->""")
        if corner == "1":
            return (0, 0)
        elif corner == "2":
            return (0, self.map_size - 1)
        elif corner == "3":
            return (self.map_size - 1, 0)
        elif corner == "4":
            return (self.map_size - 1, self.map_size - 1)

    # This function print dungeon for user
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

    def move(self, direction, coordinates):  # Hero can go outside the grid. No exception
        x = coordinates[0]
        y = coordinates[1]
        if direction.lower() == "w":
            x -= 1
        elif direction.lower() == "a":
            y -= 1
        elif direction.lower() == "d":
            y += 1
        elif direction.lower() == "s":
            x += 1

        return (x, y)


# Object Room selfgenerate monsters and treasures
class Room:
    def __init__(self, x, y):
        self.coordinates = (x, y)
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


def print_move():
    print("CHOOSE DIRECTION TO GO")
    print("North- N")
    print("West- W")
    print("East- E")
    print("South- S")
    direction = ""
    f = True
    while f:
        directions = ["n", "w", "e", "s"]
        direction = input("--->")

        if direction.lower() not in directions:
            print("You have to tape N,W,E or S")

        else:
            f = False

    return direction.lower()


# Sorting method for list of monster that then rolls die and return a Descending list according to dice roll
def sort(monsterList):
    templist = []
    for monster in range(len(monsterList)):
        rolled_monster = die.die(monsterList[monster].initiative)
        templist.append(rolled_monster)  # Using attribute initiative; rolls die
    zipped_pairs = zip(templist, monsterList)
    sortedMonsters = [x for _, x in sorted(zipped_pairs)]  # Sorts monsters in ascending order according to dice roll
    sortedMonsters.reverse()  # Reverses to make list in Descending order
    return sortedMonsters


def coinCount(treasureList):
    counter = 0
    for i in range(len(treasureList)):        
        print(f"Treasure found! {treasureList[i].name} worth {treasureList[i].value}g")
        counter += treasureList[i].value

    print(f"Treasures collected! Worth in total: {counter}g")
    return counter


def check(hero, ds, coordinates):  # Calls attack if there're monsters in the room, Calls coinCount if there're treasures; else: room empty
    x = coordinates[0]
    y = coordinates[1]

    m = ds.dungeon[x][y].monsters
    t = ds.dungeon[x][y].treasure

    return m, t

    #if ds.dungeon[x][y].monsters:  # True if sequence/list contains values
     #   print(f"Monsters: {ds.dungeon[x][y].monsters}\n{ds.dungeon[x][y].treasure}")
        #choice = input("1. Attack\n2. Escape")
        #if choice == '1':
        #    battle.attack(hero, sort(ds.dungeon[x][y].monsters))
        #elif choice == '2':
         #   battle.escape(hero, sort(ds.dungeon[x][y].monsters))

    #if ds.dungeon[x][y].treasure:  # True if sequence/list contains values
     #   print(f"There're treasures!\n{ds.dungeon[x][y].treasure}")
      #  coinCount(ds.dungeon[x][y].treasure)
    #else:
     #   print("Room empty!")
        # TODO Room.empty = True
        # TODO Room.marker = "[Empty]"

