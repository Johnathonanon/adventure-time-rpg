import enquiries


def start():
    """
    Starts game and prompts player for name
    """
    print("\nWelcome Adventurer!\n")
    print("What is your name?\n")
    global name
    name = input("My name is: ")
    print(f"\nWelcome {name}.")

    while True:

        start_prompt = input("\nAre you ready to begin? y/n ").lower()

        if start_prompt == "y":
            print("\nExcellent, Lets go!")
            select_class()
            return False
        elif start_prompt == "n":
            abort_game()
            return False
        else:
            print("\nPlease enter either 'y' or 'n'")


def select_class():
    print("\nFirst please choose a class.\n")

    classes = ['Warrior', 'Wizard', 'Archer']
    choice = enquiries.choose('Choose one of these options: ', classes)

    print(choice)


def abort_game():
    print("\nWell that's a pity :( Bye Bye")


start()