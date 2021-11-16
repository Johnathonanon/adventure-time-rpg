import random

import enquiries


class Player():
    """
    Main player class. Sets name, player class, hp, and attack.
    Has methods for progressing through dungeon, exploring, interacting
    and attacking
    """
    def __init__(self, name, player_class, health_points, attack):
        self.name = name
        self.player_class = player_class
        self.health_points = health_points
        self.attack = attack

    @classmethod
    def build_player(cls):

        name = input("Please enter your name: ")
        classes = ['Warrior', 'Wizard', 'Archer']
        player_class = enquiries.choose('\nPlease choose a class:\n', classes)

        if player_class == 'Warrior':
            health_points = random.randint(40, 50)
            attack = random.randint(5, 10)
        elif player_class == 'Wizard':
            health_points = random.randint(20, 30)
            attack = random.randint(15, 20)
        else:
            health_points = random.randint(30, 40)
            attack = random.randint(10, 15)

        print("\n****************************************")
        print(
            f"Welcome {name}!\n"
            f"You are playing as the {player_class}\n"
            f"Your HP is {health_points}\n"
            f"You have an attack of {attack}")
        print("****************************************\n")

        run_game()

        return cls(name, player_class, health_points, attack)


class Monster():
    """
    Main monster class. Sets monster class, hp, and attack.
    Has method for attacking player
    """
    def __init__(self, monster_class, health_points, attack):
        self.monster_class = monster_class
        self.health_points = health_points
        self.attack = attack

    @classmethod
    def build_monster(cls):

        monster_classes = ['Skeleton', 'Zombie', 'Goblin']

        monster_class = random.choice(monster_classes)

        if monster_class == 'Zombie':
            health_points = random.randint(40, 50)
            attack = random.randint(5, 10)
        elif monster_class == 'Skeleton':
            health_points = random.randint(20, 30)
            attack = random.randint(15, 20)
        else:
            health_points = random.randint(30, 40)
            attack = random.randint(10, 15)

        print("\n****************************************")
        print(
            f"Monster is {monster_class}\n"
            f"HP is {health_points}\n"
            f"Attack is {attack}")
        print("****************************************\n")

        return cls(monster_class, health_points, attack)


def start():
    """
    Starts game and confirms user wishes to play
    """
    print("\nWelcome Adventurer!\n")

    while True:

        start_prompt = input("\nAre you ready to begin? y/n ").lower()

        if start_prompt == "y":
            print("\nExcellent, Lets go!\n")
            Player.build_player()
            return False
        elif start_prompt == "n":
            abort_game()
            return False
        else:
            print("\nPlease enter either 'y' or 'n'")


def run_game():
    print(Monster.build_monster())


def abort_game():
    print("\nWell that's a pity :( Bye Bye")


start()