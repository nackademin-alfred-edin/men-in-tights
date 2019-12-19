import die
import random
import time
import Heroes
import menu


def attack(hero, list_of_monsters): #TODO Endurance to be change to Stamina to match other changes
    menu.clear()
    menu.printLogo()
    
    #for monster in range(len(list_of_monsters)):
    while list_of_monsters:
        input(f"""
                                        BATTLE ENTERED AGAINST A {list_of_monsters[0].name}!

                                          Press any key to roll dice""")
        menu.clear()
        menu.printLogo()
        print("""           
                                                                    (User turn)""")
        
        menu.roll_dice()
        time.sleep(1)
        menu.clear()
        menu.printLogo()
        print("""
                                                                    (User turn)""")

        go = True
        shield_block = True
        while go:
            #print(f"""
             #       {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")

            time.sleep(0.8)

            if die.die(hero.attack) > die.die(list_of_monsters[0].agility):
                if isinstance(hero, Heroes.Thief) and (random.randint(0, 100) <= 25): #Thief Special Ability
                    print("""
                                    As Thief you inflicted Critical Damage! Causing 2 Damage!""")
                    list_of_monsters[0].endurance -= 2
                else: # If Hero's attack is larger than monster's agility, inflict 1 dmg
                    menu.clear()
                    menu.printLogo()
                    print("""           
                                                                    (User turn)""")
                    print(f"""
                    {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")
                    print("""

                                Succesful roll! Monster takes 1 damage
                    """)
                    input("""
                                    Press any key to roll again""")
                    menu.clear()
                    menu.printLogo()
                    menu.roll_dice()
                    time.sleep(1)
                    list_of_monsters[0].endurance -= 1
                
                menu.clear()
                menu.printLogo()
                
                print(f"""
                    {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")
                time.sleep(0.8)
                if list_of_monsters[0].endurance <= 0:
                    menu.clear()
                    menu.printLogo()
                    print("""           
                                                                    (User turn)""")
                    print(f"""
                    {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")
                    print(f"""
                                          {list_of_monsters[0].name} slain!""")
                    del list_of_monsters[0]
                    time.sleep(0.8)
                    go = False
                    break
            else:
                print("""           
                                                                (User turn)""")
                print("""
                                            Your attack missed!""")

            
            if die.die(list_of_monsters[0].attack) > die.die(hero.agility):
                menu.clear()
                menu.printLogo
                print("Enemy turn"  )
                print(f"""
                    {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")


                print("\nMonster attacks you for 1 damage!")
                time.sleep(2)
                if isinstance(hero, Heroes.Knight) and shield_block == True: #Knight special abilitie
                    print("First attck blocked")
                    shield_block = False
                else:
                    hero.endurance -= 1
                print(f"Health after attack {hero.endurance}")
            elif list_of_monsters[0].endurance > 0:
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
