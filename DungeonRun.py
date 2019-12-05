import random


class Heroes:
    def __init__(self, name, initiative, endurance, attack, agility):
        self.name = name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility


class Knight(Heroes):
    def __init__(self):
        super().__init__(name=input("What is the name of your hero?"),
                         initiative=5, endurance=9, attack=6, agility=4)


class Wizard(Heroes):
    def __init__(self):
        super().__init__(name=input("What is the name of your hero?"),
                         initiative=6, endurance=4, attack=9, agility=5)


class Thief(Heroes):
    def __init__(self):
        super().__init__(name=input("What is the name of your hero?"),
                         initiative=7, endurance=5, attack=5, agility=7)

