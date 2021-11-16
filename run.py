import random

import enquiries


class Player():
    """
    Main player class. Sets name, player class, hp, and attack.
    Has methods for progressing through dungeon, exploring, interacting,
    fleeing and attacking
    """
    def __init__(self, name, player_class, health_points, attack):
        self.name = name
        self.player_class = player_class
        self.health_points = health_points
        self.attack = attack

    @classmethod
    def build_player(cls):
        """
        Builds player character
        """
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
        """
        Creates monster instance. One of 3 random classes.
        Sets HP and attack based on monster_class.
        """
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


class Room():
    """
    Main room class, builds instance of room as player progresses through game.
    Sets room_class, ID, and size.
    Has method describing room to player
    """
    def __init__(self, room_class, identifier, size):
        self.room_class = room_class
        self.identifier = identifier
        self.size = size


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


def prompt_user():
    """
    Prompts user to select a command and progresses game
    """
    print("What would you like to do?")

    player_choices = ["continue", "inspect", "attack", "interact", "flee"]
    choice = enquiries.choose("", player_choices)

    if choice == "continue":
        print("You continue forward")
    elif choice == "inspect":
        print("You inspect you surroundings")


def run_game():
    """
    Main function progressing through game.
    """
    print("Since the day you were old enough to wish to be something,"
          " you wished to be an Adventurer."
          " One of those brave and special souls"
          " who stand steadfast against the dangers of the world,"
          " and make life better for all."
          " While also being handsomely rewarded of course."
          " You have taken your first job, a dungeon clearance,"
          " and at present you are standing at the entrance,"
          " bracing yourself for what's to come."
          " As a beginner job this should be easy, shouldn't it?\n"
          "\nOnward Adventurer! \nTo Glory!\n"
          "\nYou enter the dungeon\n")

    prompt_user()


def abort_game():
    """
    Aborts game on user prompt
    """
    print("\nWell that's a pity :( Bye Bye")


start()
