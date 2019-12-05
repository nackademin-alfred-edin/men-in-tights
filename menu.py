#TODO Import Class files

def Knight():
    print("You've choosen 'Knight'!")

def Wizard():
    print("You've choosen 'Wizard'!")

def Thief():
    print("You've choosen 'Thief'!")

def Saved():
    print("Select Saved Hero: ")

def main():
    print("""\n\
       WELCOME TO 'Dungeon Run'!

    Start by choosing your hero, or load a previous saved hero
    1. Knight
    2. Wizard
    3. Thief

    4. Load Saved Hero
\n""")
    choice = input("Enter number for Hero: ")
    choice_menu =  {'1': Knight,
                    '2': Wizard,
                    '3': Thief,
                    '4': Saved}
    if choice not in choice_menu.keys():
        print("Please choose a hero ")
    else:
        choice_menu[choice]()


if __name__ == "__main__":
    main()