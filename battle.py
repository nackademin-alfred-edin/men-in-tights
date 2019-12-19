import die
import random
import time
import Heroes
import menu


def attack(hero, list_of_monsters): #TODO Endurance to be change to Stamina to match other changes
    menu.clear()
    menu.printLogo()
    
    for monster in range(len(list_of_monsters)):
        input(f"""
                                        BATTLE ENTERED AGAINST A {list_of_monsters[monster].name}!

                                            Press any key to roll dice""")
        menu.clear()
        menu.printLogo()
        
        menu.roll_dice()
        time.sleep(1)
        menu.clear()
        menu.printLogo()

        go = True
        
        shield_block = True
        while go:
            print(f"""
                                         {list_of_monsters[monster].name} health: {list_of_monsters[monster].endurance}""")
            time.sleep(0.8)

            if die.die(hero.attack) > die.die(list_of_monsters[monster].agility):
                if isinstance(hero, Heroes.Thief) and (random.randint(0, 100) <= 25): #Thief Special Ability
                    print("""
                                    As Thief you inflicted Critical Damage! Causing 2 Damage!""")
                    list_of_monsters[monster].endurance -= 2
                else:
                    print("""
                                    Succesful roll! Monster takes 1 damage""")
                    list_of_monsters[monster].endurance -= 1
                # If Hero's attack is larger than monster's agility, inflict 1 dmg
                print("""
                                    Succesful roll! Monster takes 1 damage""")
                list_of_monsters[monster].endurance -= 1
                time.sleep(0.8)
                print(f"""
                                        {list_of_monsters[monster].name} health after attack: {list_of_monsters[monster].endurance}""")
                time.sleep(0.8)
                if list_of_monsters[monster].endurance <= 0:
                    print(f"""
                                        {list_of_monsters[monster].name} slain!""")
                    time.sleep(0.8)
                    go = False
            else:
                print("Hero Attack missed!\n")

            
            if die.die(list_of_monsters[monster].attack) > die.die(hero.agility):
                print("\nMonster attacks you for 1 damage!")
                if isinstance(hero, Heroes.Knight) and shield_block == True: #Knight special abilitie
                    print("First attck blocked")
                    shield_block = False
                else:
                    hero.endurance -= 1
                print(f"Health after attack {hero.endurance}")
            elif list_of_monsters[monster].endurance > 0:
                print("Monster attack missed")
            if hero.endurance == 0:
                go = False
                #game_over()


def escape(hero, list_of_monsters):

    escape_chance = hero.agility * 10
    if isinstance(hero, Heroes.Wizard): #Wizard Special Ability
        escape_chance = 80

    print(f"Your chance to escape: {escape_chance}%")

    var = random.randint(0, 100)
    
    print(f"Probability: {var}")
    
    if var <= escape_chance:
        print(f"Roll Succes! \nYou've escaped!")
    
        #TODO Go back to previous room
    else:
        print("Roll Failed! \nCannot escape!!!")
        time.sleep(2)
        attack(hero, list_of_monsters)
