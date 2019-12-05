from random import randint

#get random coordinates for place functions
def get_room(map_size):
    x = randint(map_size - 1)
    y = randint(map_size - 1)
    return x, y


class Dungeon:
    def __init__(self, map_size):
        self.dungeon = generate_map(map_size)

    def generate_map(map_size):
        room = [] #empty list 
        return [[room*map_size for i in range(map_size)] for j in range(map_size)]



#TODO place_treasure() and place_monster()