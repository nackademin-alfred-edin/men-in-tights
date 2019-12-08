from random import randint
import color




class Dungeon:
    def __init__(self, map_size):
        self.map_size = map_size
        self.dungeon = self.generate_map(map_size)

    def generate_map(self, map_size):
        room = [] #empty list 
        return [[room*map_size for i in range(map_size)] for j in range(map_size)]
    
    def get_room(self, map_size):
        x = randint(map_size - 1)
        y = randint(map_size - 1)
        return dungeon[x][y]

    def print_dungeon(self, x, y):
        dungeon[x][y] = "[O]"
        for i in range(map_size):
            for j in range(map_size):
                x = ""
                if j == map_size - 1:
                    x = "\n"
                if dungeon[i][j] == "[O]":
                    print(color.fg.orange, dungeon[i][j], end=x)
                else:
                    print(color.fg.purple, dungeon[i][j], end=x)

#TODO place_treasure() and place_monster()