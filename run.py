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

        player = cls(name, player_class, health_points, attack)

        return player


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
    Sets room_is and monster_presence
    """
    def __init__(self, room_id, monster_presence):
        self.room_id = room_id
        self.monster_presence = monster_presence


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
            run_game()
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
        if Room.room_id == 6:
            time.sleep(1)
            print("\nThe door is shut and there is no way out!\n"
                  "Maybe try inspecting your surroundings...\n")
            prompt_user()
        else:
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
              "\nOnward Mighty Adventurer! \nTo Glory!\n"
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
            print("\nForward or right.\n"
                  "That's it.\n"
                  "Two choices.\n"
                  "Forward or right.")
            run_game()
    elif Room.room_id == 5:
        print("\nThere are two exits from this room.\n"
              "One to your left, halfway down the room,\n"
              "and one on you right, at the very end.")
        door_choice = input("\nWhich way will you go? left/right :").lower()
        if door_choice == "left":
            print("\nYou exit through the left hand door,\n"
                  "and enter another long dimly lit corridor.\n"
                  "After a few minutes of walking\n"
                  "you find yourself at a junction.\n"
                  "The left path continues to what appears\n"
                  "to be a blank wall in the distance,\n"
                  "however, that way gives you a sense of excitement.\n"
                  "The right stretches farther than you can see,\n"
                  "but you can barely make out a blue-ish glow\n"
                  "right at the end of the path.\n"
                  "This way gives you a feeling of home.\n")
            door_choice = input("\nWhich way? left/right :").lower()
            if door_choice == "left":
                Room.room_id = 7
                print("\nYou decide to take the left path,\n"
                      "and eventually you come to a right corner,\n"
                      "around which you can feel a very slight breeze.\n"
                      "You continue onwards and approach the next room,\n"
                      "the light of which is shining brightly.\n"
                      "Before you enter you scan the room for threats\n"
                      "but see nothing...\n"
                      "You cautiously enter...\n")
            elif door_choice == "right":
                Room.room_id = 6
                print("\nYou decide to take the right branch,"
                      "and slowly but surely you can see\n"
                      "the blue glow in the distance is getting brighter.\n"
                      "As you get closer the air seems to crackle,\n"
                      "and your hair begins to stand slightly on end.\n"
                      "Eventually you reach the entrance to the next room,\n"
                      "just to find that there is a haze\n"
                      "blocking your view of the room beyond.\n"
                      "It feels like you are looking through frosted glass,\n"
                      "with little visible except that blue glow.\n"
                      "Your curiosity trumps your hesitation,\n"
                      "and you step forward through the haze.\n"
                      "As you do, the haze solidifies,\n"
                      "and you realise you will not be returning that way.\n")
                prompt_user()
            else:
                print("\nYou have a bout of indecision,and end up\n"
                      "running headlong into the wall in front of you.\n"
                      "A strange repulsive force sends you hurtling\n"
                      " backwards down the way you just came\n"
                      "and back into the previous room.")
                run_game()
        elif door_choice == "right":
            print("\nDespite your misgivings, you decide to take\n"
                  "the doorway in the far right corner of the room.\n"
                  "It enters into a dark passageway,\n"
                  "the end of which cannot be seen.\n"
                  "As you cautiously shuffle forward in the dark,\n"
                  "you eventually reach a right turn in the tunnel,\n"
                  "and as you proceed on\n"
                  "you feel like you can hear a deep rumbling.\n"
                  "You continue forward and eventually\n"
                  "you can tell you have entered another room.\n"
                  "In the dark, you can barely make out the fact that it is\n"
                  "cylindrical, and the rumbling has gotten louder.\n"
                  "Just as you're about to retreat,\n"
                  "a door slams shut behind you,\n"
                  "and with a deafening grating noise\n"
                  "the floor gives way beneath you.\n"
                  "Your last thought is regret you didn't make it further.\n")
            abort_game()
        else:
            print("Once again, only two choices.\n"
                  "I wish I could give you another option,\n"
                  "but alas I'm just a voice in your head...")
            run_game()
    elif Room.room_id == 6:
        print("no")


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
              "Similar to the last room, this door\n"
              "emits an extremely ominous air.\n"
              "Once again, the veins of light are present,\n"
              "flowing towards the two enemies.\n"
              "And once again neither looks particularly happy\n")
        prompt_user()
    elif Room.room_id == 6:
        print("\nYou are standing just inside the doorway,\n"
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
              "You feel the hairs rise on your arms as you approach.\n")
        prompt_user()
    elif Room.room_id == 7:
        print("You are standing in a brightly lit circular room,\n"
              "smaller than any so far.\n"
              "To the right of the room, not visible from the hallway,\n"
              "is a small waterfall, flowing into a basin."
              "There's a small wooden cup sitting on the side of the basin,\n"
              "and a plaque that reads:\n"
              "****************************************\n"
              "REST WEARY ADVENTURER AND TAKE A DRINK\n"
              "FOR THE NEXT ROOM WILL PUSH YOU TO THE BRINK\n"
              "****************************************\n")
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
    elif Room.room_id == 7:
        print("\nYou hesitantly approach the blue disc.\n"
              "")


def abort_game():
    """
    Aborts game on user prompt
    """
    print("\nWell that's a pity :( Bye Bye")


start()