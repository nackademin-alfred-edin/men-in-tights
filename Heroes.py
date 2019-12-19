import random
import menu


class Heroes:
    def __init__(self, initiative, endurance, attack, agility, points):
        #self.name = name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.points = points


class Knight(Heroes):
    def __init__(self):
        super().__init__(initiative=5, endurance=9, attack=6, agility=4, points=0)


class Wizard(Heroes):
    def __init__(self):
        super().__init__(initiative=6, endurance=4, attack=9, agility=5, points=0)


class Thief(Heroes):
    def __init__(self):
        super().__init__(initiative=7, endurance=5, attack=5, agility=7, points=0)