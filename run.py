import enquiries

from random import randint


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

    @classmethod
    def build_player(cls):
        name = input("Please enter your name: ")
        classes = ['Warrior', 'Wizard', 'Archer']
        player_class = enquiries.choose('Please choose a class:\n', classes)

        return cls(name, player_class)


def start():
    """
    Starts game and confirms user wishes to play
    """
    print("\nWelcome Adventurer!\n")

    while True:

        start_prompt = input("\nAre you ready to begin? y/n ").lower()

        if start_prompt == "y":
            print("\nExcellent, Lets go!\n")
            # create_player()
            return False
        elif start_prompt == "n":
            abort_game()
            return False
        else:
            print("\nPlease enter either 'y' or 'n'")


def abort_game():
    print("\nWell that's a pity :( Bye Bye")


start()
