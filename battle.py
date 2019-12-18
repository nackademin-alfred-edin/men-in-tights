import Heroes
import die
import monster_class
import random

#hero = Heroes.Knight()
#monster = monster_class.Spider()


def attack(hero, monster): #TODO Endurance to be change to Stamina to match other changes
#IF: monster.endurance <= 0, battle won
    for monster in range(list_of_monsters):
        go = True
        while go == True:
            print(f"Monster's Stamina: {monster.endurance}")
            if die.die(hero.attack) > die.die(monster.agility): #If Hero's attack is larger than monster's agility, inflict 1 dmg
                print("\nSuccesful roll! Monster takes 1 damage")
                monster.endurance -= 1
                print("Stamina after attack: ", monster.endurance)
                if monster.endurance == 0:
                    print("\nMonster slain!")
                    go = False
            else:
                print("Attack missed!")

            elif: die.die(monster.attack) > die.die(hero.agility):
                print("\nMonster attacks you for 1 damage!")
                hero.endurance -= 1
                print(f"Health after attack {hero.endurance}")
                #if hero.endurance == 0:
                #   go = False
                #   game_over() 

def escape(hero):
    escape_chance = hero.agility * 10
    print(f"Your chance to escape: {escape_chance}%")
    var = random.randint(0, 100)
    #print(f"Probability: {var}") 
    if var <= escape_chance:
        print(f"Roll Succes! \nYou've escaped!")
    else:
        print("Roll Failed! \nCannot escape")

escape(hero)
print("\n")
attack(hero, monster)