import Heroes
import die
import monster_class
import random

hero = Heroes.Knight()
monster = monster_class.Spider()


def attack(hero, monster):
#IF: monster.endurance <= 0, battle won
    print(f"Monster's Stamina: {monster.endurance}")
    if die.die(hero.attack) > die.die(monster.agility):
        print("\nSuccesful roll! Monster takes 1 damage")
        monster.endurance -= 1  #TODO Endurance to be change to Stamina to match other changes
        print("Stamina after attack: ", monster.endurance)
    else:
        print("Attack missed!")

def escape(hero):
    escape_chance = hero.agility * 10
    print(f"Your chance to escape: {escape_chance}%")
    var = random.randint(0, 100)
    #print(f"Probability: {var}") 
    if var <= escape_chance:
        print(f"Succes! \nYou've escaped!")
    else:
        print("Failed! \nCannot escape")

escape(hero)
print("\n")
attack(hero, monster)