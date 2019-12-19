import die
import random
import time
import Heroes
import menu


def attack(hero, list_of_monsters): #TODO Endurance to be change to Stamina to match other changes
    menu.clear()
    menu.printLogo()

    while list_of_monsters:
        input(f"""
                                You charge heroically towards the {list_of_monsters[0].name}!

                                        Press any key to enter battle""")
        menu.clear()
        menu.printLogo()
        print("""           
                                                                    (User turn)""")
        
        menu.roll_dice()
        time.sleep(1)
        menu.clear()
        menu.printLogo()

        go = True
        shield_block = True
        while go:
            if die.die(hero.attack) > die.die(list_of_monsters[0].agility):
                if isinstance(hero, Heroes.Thief) and (random.randint(0, 100) <= 25): #Thief Special Ability
                    print("""
                                    As Thief you inflicted Critical Damage! Causing 2 Damage!""")
                    list_of_monsters[0].endurance -= 2
                else: # If Hero's attack is larger than monster's agility, inflict 1 dmg
                    print("""           
                                                                    (User turn)""")

                    print(f"""
                    {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")
                    
                    print("""

                                Successfull roll! Monster takes 1 damage
                                                Nice hit!
                    """)
                    list_of_monsters[0].endurance -= 1
                    
                    time.sleep(2)
                    if list_of_monsters[0].endurance <= 0:
                        time.sleep(0.5)
                        print(f"""
                                            {list_of_monsters[0].name} slain!
                                               GG WP""")
                        del list_of_monsters[0] 
                        input("""  
                                    press any key to continue""")
                        menu.clear()
                        menu.printLogo()
                        go = False
                        break
                    else:
                        input(f"""

                                     The {list_of_monsters[0].name} swings at you!

                                   Press any key to defend yourself!""")
                    menu.clear()
                    menu.printLogo()
                    print("""
                    (Enemy turn)""")
                    menu.roll_dice()
                    time.sleep(1)

            else:
                print("""           
                                                                    (User turn)""")
                print("""
                                        Your attack missed!""")

            
            if die.die(list_of_monsters[0].attack) > die.die(hero.agility):
                #menu.clear()
                #menu.printLogo
                print("""
                    (Enemy turn)""")
                menu.roll_dice()
                time.sleep(2)
                menu.clear()
                menu.printLogo()
                print(f"""
                    {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")
                
                time.sleep(1)
                print("""
                                     Monster attacks you for 1 damage!""")
                time.sleep(2)
                menu.clear()
                menu.printLogo()
                if isinstance(hero, Heroes.Knight) and shield_block == True: #Knight special abilitie
                    print("""
                                    First attack blocked by your shield!""")
                    shield_block = False
                else:
                    hero.endurance -= 1
                    print(f"""
                    {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")
                    input("""
                                      OUCH! That hurt...

                              Press any key to start your turn""")
                    menu.clear()
                    menu.printLogo()
                    print("""           
                                                                (User turn)""")
                    menu.roll_dice()
                    time.sleep(1)
                    menu.clear()
                    menu.printLogo()
        
            elif list_of_monsters[0].endurance > 0:
                menu.clear()
                menu.printLogo()
                print("""
                    (Enemy turn)""")
                print(f"""
                    {list_of_monsters[0].name} health: {list_of_monsters[0].endurance}             VS              Your health: {hero.endurance}""")
                print("""
                                        Monster attack missed
                        """)
                time.sleep(1.5)
                input("""
                                        That was a close one!

                                    Press any key to start your turn""")
                menu.clear()
                menu.printLogo()
                print("""           
                                                                (User turn)""")
                menu.roll_dice()
                time.sleep(1)
                menu.clear()
                menu.printLogo()

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
