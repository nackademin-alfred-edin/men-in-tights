import random


class Heroes:
    def __init__(self, name, initiative, stamina, attack, agility):
        self.name = name
        self.initiative = initiative
        self.endurance = stamina
        self.attack = attack
        self.agility = agility


class Knight(Heroes):
    def __init__(self):
        super().__init__(name=input("What is the name of your hero?"),
                         initiative=5, stamina=9, attack=6, agility=4)


class Wizard(Heroes):
    def __init__(self):
        super().__init__(name=input("What is the name of your hero?"),
                         initiative=6, stamina=4, attack=9, agility=5)


class Thief(Heroes):
    def __init__(self):
        super().__init__(name=input("What is the name of your hero?"),
                         initiative=7, stamina=5, attack=5, agility=7)

