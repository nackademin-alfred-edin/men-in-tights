class Monster():
    def __init__(self, name,  initiative, endurance, attack, agility):
        self.name = name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility

class Spider(Monster):
    commonness = 20
    def __init__(self):
        super().__init__(name="Spider", initiative=7, endurance=1, attack=2, agility=3)


class Skeleton(Monster):
    commonness = 15
    def __init__(self):
        super().__init__(name="Skeleton", initiative=4, endurance=2, attack=3, agility=3)

class Orc(Monster):
    commonness = 10
    def __init__(self):
        super().__init__(name="Orc", initiative=6, endurance=3, attack=4, agility=4)

class Troll(Monster):
    commonness = 5
    def __init__(self):
        super().__init__(name="Troll", initiative=2, endurance=4, attack=7, agility=2)

class Treasure():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Coins(Treasure):
    commonness = 40
    def __init__(self):
        super().__init__ (name="Coins", value=2)

class Pouch(Treasure):
    commonness = 20
    def __init__(self):
        super().__init__ (name="Pouch", value=6)

class Jewelry(Treasure):
    commonness = 15
    def __init__(self):
        super().__init__ (name="Jewelry", value=10)

class Gemstone(Treasure):
    commonness = 10
    def __init__(self):
        super().__init__ (name="Gemstone", value=14)

class Chest(Treasure):
    commonness = 5
    def __init__(self):
        super().__init__ (name="Chest", value=20)