import enquiries


class Player():
    """
    Main player class. Sets name, player class, hp, and attack.
    Has methods for progressing through dungeon, exploring, interacting
    and attacking
    """
    def __init__(self, name, player_class, hp, attack):
        self.name = name
        self.player_class = player_class
        self.hp = hp
        self.attack = attack

    def print_name():
        print(name)


def start():
    """
    Starts game,prompts player for name and confirms progression of game
    """
    print("\nWelcome Adventurer!\n")
    print("What is your name?\n")
    global name
    name = input("My name is: ")
    print(f"\nWelcome {name}.")

    while True:

        start_prompt = input("\nAre you ready to begin? y/n ").lower()

        if start_prompt == "y":
            print("\nExcellent, Lets go!\n")
            select_class()
            return False
        elif start_prompt == "n":
            abort_game()
            return False
        else:
            print("\nPlease enter either 'y' or 'n'")


def select_class():

    classes = ['Warrior', 'Wizard', 'Archer']
    choice = enquiries.choose('First please choose a class:\n', classes)

    print(choice)


def abort_game():
    print("\nWell that's a pity :( Bye Bye")


start()