#TODO Import Class files

def main():
    print("""\n\
       WELCOME TO 'Dungeon Run'!

    Start by choosing your hero
    1. Knight
    2. Wizard
    3. Thief
\n""")
    choice = input("Enter number for Hero: ")
    choice_menu =  {'1': Knight,
                    '2': Wizard,
                    '3': Thief}
    if choice not in choice_menu.keys():
        print("Please choose a hero")
    else:
        choice_menu[choice]()


if __name__ == "__main__":
    main()