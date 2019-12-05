import color

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
    print(color.color.fg.lightblue, "    WELCOME TO ", end="")
    print(color.color.fg.red, "Dungeon Run", end="")
    print(color.color.fg.lightblue, "!", end="\n\n")
    print(color.color.fg.lightgrey, """
    Start by choosing your hero, or load a previous saved hero
    1. Knight
    2. Wizard
    3. Thief

    4. Load Saved Hero
\n""")
    print(color.color.fg.purple, "Enter number for Hero: ", end="")
    choice = input()
    choice_menu =  {'1': Knight,
                    '2': Wizard,
                    '3': Thief,
                    '4': Saved}
    if choice not in choice_menu.keys():
        print(color.color.fg.red, "Please choose a hero ")
    else:
        choice_menu[choice]()


if __name__ == "__main__":
    main()