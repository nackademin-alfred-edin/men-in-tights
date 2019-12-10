
class Monster:
    def __init__(self, initiative, endurance, attack, agility, usualness):
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.usualness = usualness

class Spider(Monster):
    def __init__(self):
        super().__init__(initiative=7, endurance=1, attack= 2, agility=3, usualness=0.2)

class Skeleton(Monster):
    def __init__(self):
        super().__init__(initiative=4, endurance=2, attack=3, agility=3, usualness=0.15)

class Orc(Monster):
    def __init__(self):
        super().__init__(initiative=6, endurance=3, attack=4, agility=4, usualness=0.1)


class Troll(Monster):
    def __init__(self):
        super().__init__(initiative=2, endurance=4, attack=7, agility=2, usualness=0.05)



