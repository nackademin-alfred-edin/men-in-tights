from random import randint
import monster_treasure as mt
import color

def print_move():
    print("CHOOSE DIRECTION TO GO")
    print("North- N")
    print("West- W")
    print("East- E")
    print("South- S")
    direction = input("--->")
    return direction.lower()


def move(direction, x, y):
    if direction == "n":
        x -= 1
    elif direction == "w":
        y -= 1
    elif direction == "e":
        y += 1
    elif direction == "s":
        x += 1
    return x, y


class Dungeon:
    def __init__(self, map_size, x, y):
        self.map_size = map_size
        self.start_room = self.start_point(x, y)
        self.dungeon = self.generate_map(self.map_size)

    def start_point(self, x, y):
        return (x, y)

    def generate_map(self, map_size):
        room = []
        dungeon = [[room * map_size for i in range(map_size)] for j in range(map_size)]
        for i in range(map_size):
            for j in range(map_size):
                if self.start_room != (i, j):
                    self.place_content(dungeon[i][j])
        return dungeon

    def fil_dungeon(self):
        for i in range(map_size):
            for j in range(map_size):
                self.place_content(self.dungeon[i][j])

    def place_content(self, room):
        content = ["spider", "skeleton", "orc", "troll", "coins", "pouch", "jewelry", "gemstone", "chest"]
        for i in content:
            if i == "spider":
                if mt.Spider.commonness >= randint(0, 100):
                    spider = mt.Spider()
                    room.append(spider)
            if i == "skeleton":
                if mt.Skeleton.commonness >= randint(0, 100):
                    skeleton = mt.Skeleton()
                    room.append(skeleton)
            if i == "orc":
                if mt.Orc.commonness >= randint(0, 100):
                    orc = mt.Orc()
                    room.append(orc)
            if i == "troll":
                if mt.Troll.commonness >= randint(0, 100):
                    troll = mt.Troll()
                    room.append(troll)
            if i == "coins":
                if mt.Coins.commonness >= randint(0, 100):
                    coins = mt.Coins()
                    room.append(coins)
            if i == "pouch":
                if mt.Pouch.commonness >= randint(0, 100):
                    pouch = mt.Pouch()
                    room.append(pouch)
            if i == "jewelry":
                if mt.Jewelry.commonness >= randint(0, 100):
                    jewelry = mt.Jewelry()
                    room.append(jewelry)
            if i == "gemstone":
                if mt.Gemstone.commonness >= randint(0, 100):
                    gemstone = mt.Gemstone()
                    room.append(gemstone)
            if i == "chest":
                if mt.Chest.commonness >= randint(0, 100):
                    chest = mt.Chest()
                    room.append(chest)

    # This function print dungeon for user
    def print_dungeon(self, x, y):
        room = "[X]"
        dungeon = [[room for i in range(self.map_size)] for j in range(self.map_size)]
        dungeon[x][y] = "[O]"
        for i in range(self.map_size):
            for j in range(self.map_size):
                x = ""
                if j == self.map_size - 1:
                    x = "\n"
                if dungeon[i][j] == "[O]":
                    print(color.color.fg.orange, dungeon[i][j], end=x)
                else:
                    print(color.color.fg.purple, dungeon[i][j], end=x + color.color.fg.reset)
