import random

import time

import enquiries


room_list = [
    {"progress_text": "bla",
     "description": "\nYou find your self in a large stone room,\n"
                    "3 times as wide as it is long.\n"
                    "It's dark, but there appears to be some sort\n"
                    "of ethereal light coming from the stone itself.\n"
                    "This place is old,\nthere's a thick layer of dust,\n"
                    "and the air is stale.\n"
                    "There are statues lined at even intervals,\n"
                    "standing like sentinels around the perimeter.\n"
                    "The only exit is directly in front of you.\n",
     "interaction": "\nThere doesn't seem to be much to do in this room.\n"
                    "It appears to be the entrance chamber of this dungeon.\n"
                    "Maybe you should continue on?\n",
     "monster_presence": 0,
     "direction_choices": {
         "forward": 2
     }},
    {"description": "\nYou are in a room roughly half the size of the first.\n"
                    "This room is the most brightly lit area so far.\n"
                    "It's made from the same stone as everywhere else,\n"
                    "except for what resembles narrow veins of pulsing light\n"
                    " flowing from the walls to the center of the room.\n"
                    "In the center stands a very unhappy looking monster.\n"
                    "There are two exits from the room,\none straight ahead\n"
                    "and one to the right.\nThe one straight ahead has a\n"
                    "very ominous air coming from it. The right less so.\n"
                    "It seems apparent you won't be going anywhere\nwith"
                    " the monster blocking your way.\n",
     "interaction": "\nThe only thing to possibly interact with\n"
                    "is the monster, which is staring at you\n"
                    "with what can only be described as violent intent.\n"
                    "Attacking would be a better bet\n",
     "monster_presence": 1,
     "direction_choices": {
         "forward": 3,
         "right": 4
     }},
    {"description": "none",
     "interaction": "none",
     "monster_presence": 0,
     "direction_choices": "none"},
    {"description": "\nYou find yourself at one end of a long narrow room.\n"
                    "It perfectly resembles the previous room,\n"
                    "except for the different dimenions.\n"
                    "Directly in front of you,\nroughly a quarter"
                    " the way down the long room,\nstands a monster.\n"
                    "And roughy halfway,\nin front of the first"
                    " visible exit,\nstands another.\n"
                    "The second exit from the room is"
                    " at the very end,\nin the right corner.\n"
                    "Similar to the last room, this door\n"
                    "emits an extremely ominous air.\n"
                    "Once again, the veins of light are present,\n"
                    "flowing towards the two enemies.\n"
                    "And once again neither looks particularly happy\n",
     "interaction": "\nOnce again the only seemingly interactable objects\n"
                    "in this room are both animated and very agressive.\n"
                    "This is no place for pacifists unfortunately.\n",
     "monster_presence": 1,
     "direction_choices": {
         "left": 6,
         "right": 5
     }},
    {"description": "none",
     "interaction": "none",
     "monster_presence": 0,
     "direction_choices": "none"},
    {"description": "\nYou are standing just inside the doorway,\n"
                    "at the end of what appears to be a stone bridge.\n"
                    "The room appears square,\n"
                    "and you have entered at one of the corners.\n"
                    "Glancing upwards, the room doesn't"
                    " appear to have a ceiling,\n"
                    "just a darkness stretching infinitely to the heavens.\n"
                    "Similarly, peeking cautiously over"
                    " the edge of the 'bridge'\n"
                    "shows a dark chasm reaching down"
                    " into the bowels of the earth."
                    "At the end of the walkway is a platform.\n"
                    "And on that platfrom is a strange floating blue disc.\n"
                    "It's approximately twice your height,\n"
                    "and made of what looks like rolling magical vapor.\n"
                    "You feel the hairs rise on your arms as you approach.\n",
     "interaction": "\nYou hesitantly approach the"
                    " blue disc in front of you.\n"
                    "If it wasn't for the fact you are trapped in here,\n"
                    "you would be less than enthusiastic about interacting\n"
                    "with some strange, evidently magical, object.\n"
                    "As you get nearer the disc seems to\n"
                    "start exerting a pulling force on you.\n"
                    "The force drags you closer and closer,\n"
                    "until finally a wisp of your clothing\n"
                    "is touched by the swirling blue vapor.\n"
                    "There is a flash of light,\n"
                    "and a sound like a wind chime,\n"
                    "and you find yourself back at the dungeon entrance...\n"
                    "You feel a strange sense of deja vu.",
     "monster_presence": 0,
     "direction_choices": "none"},
    {"description": "You are standing in a brightly lit circular room,\n"
                    "smaller than any so far.\n"
                    "To the right of the room, not visible from the hallway,\n"
                    "is a small waterfall, flowing into a basin."
                    "There's a small wooden cup"
                    " sitting on the side of the basin,\n"
                    "and a plaque that reads:\n"
                    "****************************************\n"
                    "REST WEARY ADVENTURER AND TAKE A DRINK\n"
                    "FOR THE NEXT ROOM WILL PUSH YOU TO THE BRINK\n"
                    "****************************************\n",
     "interaction": "room 7 interaction",
     "monster_presence": 0,
     "direction_choices": {
         "forward": 8
     }},
    {"description": "room 8",
     "interaction": "",
     "monster_presence": 1,
     "direction_choices": ""}
]


class Player():
    """
    Main player class. Sets name, player class, hp, and attack.
    Has methods for progressing through dungeon, exploring, interacting,
    fleeing and attacking
    """
    def __init__(self, player_name, player_class):
        self.player_name = player_name
        self.player_class = player_class


class Monster():
    """
    Main monster class. Sets monster class, hp, and attack.
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
    Sets room_id and monster_presence
    """
    def __init__(self, room_id, monster_presence):
        self.room_id = room_id
        self.monster_presence = monster_presence


def start():
    """
    Starts game and confirms user wishes to play
    """
    player_name = input("\nPlease enter your name: ")

    print("\nPlease choose a class:")

    player_classes = ["Archer", "Warrior", "Wizard"]
    player_class = enquiries.choose("", player_classes)

    player = Player(player_name, player_class)

    print(f"\nWelcome {player_name}!\n"
          "\nEver since you were old enough to\n"
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
          f"\nOnward Mighty {player_class}! \nTo Glory!\n"
          "\nYou enter the dungeon\n")

    prompt_user()


def prompt_user():
    """
    Prompts user to select a command and progresses game
    """
    print("\nWhat would you like to do?")

    player_choices = ["Continue", "Inspect", "Attack", "Interact", "Flee"]
    choice = enquiries.choose("", player_choices)

    current_room = 0

    if choice == "Continue":
        if room_list[current_room]["monster_presence"] == 0:
            time.sleep(1)
            print("\nWhich direction would you like to go?")
            direction_choices = room_list[current_room]["direction_choices"]
            direction_choice = enquiries.choose("", direction_choices)
            direction_choice = current_room
            run_game(current_room)
        else:
            print("You must defeat the monster to proceed")
            prompt_user()
    elif choice == "Inspect":
        inspect_room(current_room)
    elif choice == "Attack":
        run_battle()
    elif choice == "Interact":
        player_interact()
    else:
        abort_game()


def run_game(current_room):
    """
    Moves players through game while giving brief description
    """
    time.sleep(1)
    print(room_list[current_room]["progress_text"])
    prompt_user()


def inspect_room(current_room):
    """
    When user selects 'Inspect' prints a brief description
    of the current room, then prompts the player once more.
    Description is different for each room depending on unique ID
    """
    print("\nYou inspect your surroundings...\n")

    time.sleep(1)
    print(room_list[current_room]["description"])
    prompt_user()


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
        print()
        prompt_user()
    elif Room.room_id == 2:
        print()
        prompt_user()
    elif Room.room_id == 4:
        print()
        prompt_user()
    elif Room.room_id == 6:
        print()
        Room.room_id = 1
        prompt_user()


def abort_game():
    """
    Aborts game on user prompt
    """
    print("\nWell that's a pity :( Bye Bye")


start()