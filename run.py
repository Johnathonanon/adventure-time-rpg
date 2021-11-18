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

        Room.room_id = 1

        run_game()

        player = cls(name, player_class, health_points, attack)

        return player


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
    def __init__(self, room_class, room_id, size):
        self.room_class = room_class
        self.room_id = room_id
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

    player_choices = ["Continue", "Inspect", "Attack", "Interact", "Flee"]
    choice = enquiries.choose("", player_choices)

    if Room.room_id == 1:
        if choice == "Continue":
            Room.room_id = 2
            run_game()
        elif choice == "Inspect":
            inspect_room()
        elif choice == "Attack":
            run_battle()


def run_game():
    """
    Main function progressing through game.
    """
    if Room.room_id == 1:
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

    elif Room.room_id == 2:
        print("\nYou continue forward through the only visible doorway,"
              " and find yourself in a long stone corridor."
              " The corridor also gives off a dull ambient light,"
              " evidently magical in nature,"
              " which is just barely enough to see by."
              " It's obviously very old, with years of accumulated dust,"
              " and cobwebs hanging from ceilings and corners."
              " You come to a left turn in the passage and continue on,"
              " as it's the only way to go."
              " Ahead you can see a doorway into a room"
              " far brighter than the hallway you're presently in."
              " There seems to be the shadow of ...."
              " something moving around in there."
              " A frisson of nerves runs through you"
              " but you steel yourself and move forward.\n"
              "\nYou enter the room\n")
        prompt_user()


def inspect_room():
    """
    When user selects 'Inspect' prints a brief description
    of the current room, then prompts the player once more.
    Description is different for each room depending on unique ID
    """
    print("\nYou inspect your surroundings...\n")

    if Room.room_id == 1:
        print("You find your self in a large stone room,"
              " 3 times as wide as it is long."
              " It's dark, but there appears to be some sort"
              " of ethereal light coming from the stone itself."
              " This place is old, there's a thick layer of dust"
              " and the air is stale."
              " There are statues lined at even intervals"
              " around the perimeter, they look like sentinels."
              " The only exit is directly in front of you.")
        prompt_user()


def run_battle():
    """
    When user selects 'Attack' option initiates a battle between
    player and monster.
    """
    print("Fighting")


def abort_game():
    """
    Aborts game on user prompt
    """
    print("\nWell that's a pity :( Bye Bye")


start()