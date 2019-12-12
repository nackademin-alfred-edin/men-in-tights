
class Monster():
    def __init__(self, initiative, endurance, attack, agility, usualness):
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.usualness = usualness

class Spider(Monster):
    def __init__(self):
        super().__init__(initiative, endurance, attack, agility, usualness)
        self.initiative = 7
        self.endurance = 1
        self.attack = 2
        self.agility = 3
        self.usualness = 0.2


class Skeleton(Monster):
    def __init__(self):
        super().__init__(initiative, endurance, attack, agility, usualness)
        self.initiative = 4
        self.endurance = 2
        self.attack = 3
        self.agility = 3
        self.usualness = 0.15


class Orc(Monster):
    def __init__(self):
        super().__init__(initiative, endurance, attack, agility, usualness)
        self.initiative = 6
        self.endurance = 3
        self.attack = 4
        self.agility = 4
        self.usualness = 0.1


class Troll(Monster):
    def __init__(self):
        super().__init__(initiative, endurance, attack, agility, usualness)
        self.initiative = 2
        self.endurance = 4
        self.attack = 7
        self.agility = 2
        self.usualness = 0.05



