import random

import time

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

        start_prompt = input("\nAre you ready to begin? y/n :").lower()

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
    print("\nWhat would you like to do?")

    player_choices = ["Continue", "Inspect", "Attack", "Interact", "Flee"]
    choice = enquiries.choose("", player_choices)

    if choice == "Continue":
        Room.room_id = Room.room_id + 1
        run_game()
    elif choice == "Inspect":
        inspect_room()
    elif choice == "Attack":
        run_battle()
    elif choice == "Interact":
        player_interact()
    else:
        abort_game()


def run_game():
    """
    Moves players through game while giving brief description
    """
    time.sleep(1)
    if Room.room_id == 1:
        print("Ever since you were old enough to\n"
              "listen to stories and play with toys\n"
              "you have wished to be an Adventurer.\n"
              "One of those brave and special souls\n"
              "who stand steadfast against the dangers of the world,\n"
              "and make life better for all.\n"
              "While also being handsomely rewarded of course.\n"
              "You have taken your first job, a dungeon clearance,\n"
              "and at present you are standing at the entrance,\n"
              "bracing yourself for what's to come.\n"
              "As a beginner job this should be easy, shouldn't it?\n"
              "\nOnward Adventurer! \nTo Glory!\n"
              "\nYou enter the dungeon\n")
        prompt_user()
    elif Room.room_id == 2:
        print("\nYou continue forward through the only visible doorway,\n"
              "and find yourself in a long stone corridor.\n"
              "The corridor also gives off a dull ambient light,\n"
              "evidently magical in nature,\n"
              "which is just barely enough to see by.\n"
              "It's obviously very old, with years of accumulated dust,\n"
              "and cobwebs hanging from ceilings and corners.\n"
              "You come to a left turn in the passage and continue on,\n"
              "as it's the only way to go.\n"
              "Ahead you can see a doorway into a room\n"
              "far brighter than the hallway you're presently in.\n"
              "There seems to be the shadow of...\n"
              "something...\nmoving around in there.\n"
              "A frisson of nerves runs through you\n"
              "but you steel yourself and move forward.\n"
              "\nYou enter the room\n")
        prompt_user()
    elif Room.room_id == 3:
        print("\nThere are two doorways exiting this room.\n"
              "One directly in front of you behind the slain monster,\n"
              "and one to your right.")
        door_choice = input("\nWhich way will you go? forward/right :").lower()
        if door_choice == "forward":
            print("\nYou proceed through the door directly in front of you.\n"
                  "The hallway you find yourself in is the darkest yet.\n"
                  "There seems to be an ominous feeling in the air,\n"
                  "and a somewhat tangy smell assualts your nose.\n"
                  "The doorway to the room ahead appears before you,\n"
                  "and you continue on into the unknown.\n"
                  "As soon as you step foot over the threshold,\n"
                  "a door slams shut behind you,\n"
                  "sealing you from the corridor behind.\n"
                  "A hissing noise accompanies the appearance\nof"
                  " a thick luminescent green fog,\n"
                  "rapidly rising from every surface.\n"
                  "Your last thought as the world goes black\n"
                  "is how poor your luck must be,\n"
                  "but perhaps in another life you will succeed...\n")
            abort_game()
        elif door_choice == "right":
            print("\nYou proceed through the door to the right.\n"
                  "You enter a long straight corridor,\n"
                  "at the end of which you can see\n"
                  "light pouring from what is evidently the next room.\n"
                  "You continue forward cautiously,\n"
                  "and once again you can see something moving\n"
                  "ahead as you get closer to the doorway.\n"
                  "\nYou enter the next room")
            Room.room_id = 4
            prompt_user()
        else:
            print("\nForward or left.\n"
                  "That's it.\n"
                  "Two choices.\n"
                  "Forward or left")
            run_game()
    elif Room.room_id == 5:
        print("\nThere are two exits from this room.\n"
              "One to your left, halfway down the room,\n"
              "and one on you right, at the very end.")
        door_choice = input("\nWhich way will you go? left/right :").lower()
        if door_choice == "left":
            print("left")
            run_game()
        elif door_choice == "right":
            print("right")
            run_game()


def inspect_room():
    """
    When user selects 'Inspect' prints a brief description
    of the current room, then prompts the player once more.
    Description is different for each room depending on unique ID
    """
    print("\nYou inspect your surroundings...\n")

    time.sleep(1)
    if Room.room_id == 1:
        print("\nYou find your self in a large stone room,\n"
              "3 times as wide as it is long.\n"
              "It's dark, but there appears to be some sort\n"
              "of ethereal light coming from the stone itself.\n"
              "This place is old,\nthere's a thick layer of dust,\n"
              "and the air is stale.\n"
              "There are statues lined at even intervals,\n"
              "standing like sentinels around the perimeter.\n"
              "The only exit is directly in front of you.\n")
        prompt_user()
    elif Room.room_id == 2:
        print("\nYou are in a room roughly half the size of the first.\n"
              "This room is the most brightly lit area so far.\n"
              "It's made from the same stone as everywhere else,\n"
              "except for what looks like narrow veins of pulsing"
              " light\nflowing from the walls to the center of the room.\n"
              "In the center stands a very unhappy looking monster.\n"
              "There are two exits from the room,\none straight ahead\n"
              "and one to the right.\nThe one straight ahead has an\n"
              "extremely ominous air coming from it. The right less so.\n"
              "It seems apparent you won't be going anywhere\nwith"
              " the monster blocking your way.\n")
        prompt_user()
    elif Room.room_id == 4:
        print("\nYou find yourself at one end of a long narrow room.\n"
              "It perfectly resembles the previous room,\n"
              "except for the different dimenions.\n"
              "Directly in front of you,\nroughly a quarter"
              " the way down the long room,\nstands a monster.\n"
              "And roughy halfway,\nin front of the first"
              " visible exit,\nstands another.\n"
              "The second exit from the room is"
              " at the very end,\nin the right corner.\n"
              "Once again, the veins of light are present,\n"
              "flowing towards the two enemies.\n"
              "And once again neither looks particularly happy\n")
        prompt_user()
    elif Room.room_id == 5:
        print("You are standing just inside the doorway,\n"
              "at the end of what appears to be a stone bridge.\n"
              "The room appears square,\n"
              "and you have entered at one of the corners.\n"
              "Glancing upwards, the room doesn't appear to have a ceiling,\n"
              "just a darkness stretching infinitely to the heavens.\n"
              "Similarly, peeking cautiously over the edge of the 'bridge'\n"
              "shows a dark chasm reaching down into the bowels of the earth."
              "At the end of the walkway is a platform.\n"
              "And on that platfrom is a strange floating blue disc.\n"
              "It's approximately twice your height,\n"
              "and made of what looks like rolling magical vapor.\n"
              "You feel the hairs rise on your arms as you approach.")
    else:
        print("You're")


def run_battle():
    """
    When user selects 'Attack' option, initiates a battle between
    player and monster.
    """
    time.sleep(1)
    if Room.room_id == 2:
        monster1 = Monster.build_monster()
        print(f"You attack the {monster1.monster_class}")
        print(f"The {monster1.monster_class} is hurt")
        print(f"The {monster1.monster_class} is dead")
        prompt_user()
    elif Room.room_id == 4:
        monster2 = Monster.build_monster()
        monster3 = Monster.build_monster()
        print(f"\nYou are attacked by {monster2.monster_class}"
              f" and {monster3.monster_class}")
        prompt_user()
    elif Room.room_id == 8:
        print("boss fight")
        prompt_user()
    else:
        print("\nI know you're eager Adventurer...\n"
              "but there's nothing to fight...\n"
              "except perhaps your own inner demons?")
        prompt_user()


def player_interact():
    """
    Allows player to interact with environment when possible to do so
    """
    time.sleep(1)
    if Room.room_id == 1:
        print("\nThere doesn't seem to be much to do in this room.\n"
              "It appears to be the entrance chamber of this dungeon.\n"
              "Maybe you should continue on?\n")
        prompt_user()
    elif Room.room_id == 2:
        print("\nThe only thing to possibly interact with\n"
              "is the monster, which is staring at you\n"
              "with what can only be described as violent intent.\n"
              "Attacking would be a better bet\n")
        prompt_user()
    elif Room.room_id == 4:
        print("\nOnce again the only seemingly interactable objects\n"
              "in this room are both animated and very agressive.\n"
              "This is no place for pacifists unfortunately.\n")
        prompt_user()


def abort_game():
    """
    Aborts game on user prompt
    """
    print("\nWell that's a pity :( Bye Bye")


start()