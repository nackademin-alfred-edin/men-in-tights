from random import randint
import color
from time import sleep
import sys

# monsters and treasures dictionaries depends on map_size
monsters_lite = {"spider": 3, "skeleton": 2, "orc": 2, "troll": 1}
monsters_medium = {"spider": 5, "skeleton": 4, "orc": 3, "troll": 1}
monsters_big = {"spider": 13, "skeleton": 10, "orc": 6, "troll": 3}

treasures_lite = {"coins": 7, "pouch": 3, "jewelry": 2, "gemstone": 2, "chest": 1}
treasures_medium = {"coins": 10, "pouch": 5, "jewelry": 4, "gemstone": 3, "chest": 1}
treasures_big = {"coins": 25, "pouch": 13, "jewelry": 10, "gemstone": 6, "chest": 3}


def start_point():
    corner = input("""
                                        Where do you want to start?
                                            1. North west
                                            2. North east
                                            3. South west
                                            4. South east
    """)

    if corner == "1":
        dungeon[0][0] = "[O]"
    elif corner == "2":
        dungeon[0][-1]
    elif corner == "3":
        pass


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
    def __init__(self, map_size):
        self.map_size = map_size
        self.dungeon = self.generate_map(self.map_size)
        if self.map_size == 4:
            self.place_monsters(monsters_lite)
            self.place_tresure(treasures_lite)
        if self.map_size == 5:
            self.place_monsters(monsters_medium)
            self.place_tresure(treasures_medium)
        if self.map_size == 8:
            self.place_monsters(monsters_big)
            self.place_tresure(treasures_big)

    def generate_map(self, map_size):
        room = []  # empty list
        return [[room * map_size for i in range(map_size)] for j in range(map_size)]

    # Working on function "exclude corners"
    def get_room(self, map_size):
        x = randint(0, map_size - 1)
        y = randint(0, map_size - 1)
        return self.dungeon[x][y]

    def place_monsters(self, monsters_dict):
        for monster, value in monsters_dict.items():
            while value > 0:
                self.get_room(self.map_size).append(monster)
                value -= 1

    def place_tresure(self, treasure_dict):
        for treasure, value in treasure_dict.items():
            while value > 0:
                self.get_room(self.map_size).append(treasure)
                value -= 1

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
                    print(dungeon[i][j], end=x)
                else:
                    print(f"""{dungeon[i][j]}""", end=x)
                    sys.stdout.flush()
                    sleep(0.06)
