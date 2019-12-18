import die
import random
import time


def attack(hero, list_of_monsters): #TODO Endurance to be change to Stamina to match other changes
    print("\nBATTLE ENTERED!")
    for monster in range(len(list_of_monsters)):
        go = True
        while go:
            print(f"{list_of_monsters[monster].name} Stamina: {list_of_monsters[monster].endurance}")
            if die.die(hero.attack) > die.die(list_of_monsters[monster].agility):
                # If Hero's attack is larger than monster's agility, inflict 1 dmg
                print("\nSuccesful roll! Monster takes 1 damage")
                list_of_monsters[monster].endurance -= 1
                time.sleep(1)
                print(f"{list_of_monsters[monster].name} Stamina after attack: {list_of_monsters[monster].endurance}")
                if list_of_monsters[monster].endurance == 0:
                    print(f"\n{list_of_monsters[monster].name} slain!")
                    go = False
            else:
                print("\nAttack missed!\n")

            if die.die(list_of_monsters[monster].attack) > die.die(hero.agility):
                print("\nMonster attacks you for 1 damage!")
                hero.endurance -= 1
                print(f"Health after attack {hero.endurance}")
            if hero.endurance == 0:
                go = False
                #game_over()


def escape(hero, list_of_monsters):
    escape_chance = hero.agility * 10
    print(f"Your chance to escape: {escape_chance}%")
    var = random.randint(0, 100)
    print(f"Probability: {var}")
    if var <= escape_chance:
        print(f"Roll Succes! \nYou've escaped!")
        #TODO Go back to previous room
    else:
        print("Roll Failed! \nCannot escape")
        #attack(hero, list_of_monsters)

