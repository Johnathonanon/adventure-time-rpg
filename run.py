import random

import time

import enquiries


room_list = [
    {"description": "\nYou find your self in a large stone room,\n"
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
         "Forward": 1
     }},
    {"progress_text": "\nYou continue forward"
                      " through the only visible doorway,\n"
                      "and find yourself in a long stone corridor.\n"
                      "The corridor also gives off a dull ambient light,\n"
                      "evidently magical in nature,\n"
                      "which is just barely enough to see by.\n"
                      "You come to a left turn in the passage"
                      " and continue on,\n"
                      "as it's the only way to go.\n"
                      "Ahead you can see a doorway into a room\n"
                      "far brighter than the hallway you're presently in.\n"
                      "There seems to be the shadow of...\n"
                      "something...\nmoving around in there.\n"
                      "A frisson of nerves runs through you\n"
                      "but you steel yourself and move forward.\n"
                      "\nYou enter the room\n",
     "description": "\nYou are in a room roughly half the size of the first.\n"
                    "This room is the most brightly lit area so far.\n"
                    "It's made from the same stone as everywhere else,\n"
                    "except for what resembles narrow veins of pulsing light\n"
                    "flowing from the walls to the center of the room.\n"
                    "In the center stands a very unhappy looking monster.\n"
                    "There are two exits from the room,\none straight ahead\n"
                    "and one to the right.\nThe one straight ahead has a\n"
                    "very ominous air coming from it. The right less so.\n",
     "interaction": "\nThe only thing to possibly try and interact with\n"
                    "is the monster, which is ill advised...",
     "monster_presence": 1,
     "monster_class": "Skeleton",
     "monster_hp": 50,
     "monster_attack": 10,
     "direction_choices": {
         "Forward": 2,
         "Right": 3
     }},
    {"progress_text": "\nYou proceed through the door"
                      " directly in front of you.\n"
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
                      "but perhaps in another life you will succeed...\n",
     "description": "none",
     "interaction": "none",
     "monster_presence": 0,
     "direction_choices": "none"},
    {"progress_text": "\nYou proceed through the door to the right.\n"
                      "You enter a long straight corridor,\n"
                      "at the end of which you can see\n"
                      "light pouring from what is evidently the next room.\n"
                      "You continue forward cautiously,\n"
                      "and once again you can see something moving\n"
                      "ahead as you get closer to the doorway.\n"
                      "You enter the next room\n",
     "description": "\nYou find yourself at one end of a long narrow room.\n"
                    "It perfectly resembles the previous room,\n"
                    "except for the different dimensions.\n"
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
     "monster_presence": 2,
     "monster_class": "Zombie",
     "monster_hp": 60,
     "monster_attack": 15,
     "direction_choices": {
         "Left": 5,
         "Right": 4
     }},
    {"progress_text": "\nDespite your misgivings, you decide to take\n"
                      "the doorway in the far right corner of the room.\n"
                      "It enters into a dark passageway,\n"
                      "the end of which cannot be seen.\n"
                      "As you cautiously shuffle forward in the dark,\n"
                      "you eventually reach a right turn in the tunnel,\n"
                      "and as you proceed on\n"
                      "you feel like you can hear a deep rumbling.\n"
                      "You continue forward and eventually\n"
                      "you can tell you have entered another room.\n"
                      "You can barely make out the fact that it is\n"
                      "cylindrical, and the rumbling has gotten louder.\n"
                      "Just as you're about to retreat,\n"
                      "a door slams shut behind you,\n"
                      "and with a deafening grating noise\n"
                      "the floor gives way beneath you.\n"
                      "Your last thought is\n"
                      "regret you didn't make it further.",
     "description": "none",
     "interaction": "none",
     "monster_presence": 0,
     "direction_choices": "none"},
    {"progress_text": "\nYou exit through the left hand door,\n"
                      "and enter another long dimly lit corridor.\n"
                      "After a few minutes of walking\n"
                      "you find yourself at a junction.\n"
                      "The left path continues to what appears\n"
                      "to be a blank wall in the distance,\n"
                      "however, that way gives you a sense of excitement.\n"
                      "The right stretches farther than you can see,\n"
                      "but you can barely make out a blue-ish glow\n"
                      "right at the end of the path.\n"
                      "This way gives you a feeling of home.\n",
     "description": "\nYou find yourself at a junction.\n"
                    "The left path continues to what appears\n"
                    "to be a blank wall in the distance,\n"
                    "however, that way gives you a sense of excitement.\n"
                    "The right stretches farther than you can see,\n"
                    "but you can barely make out a blue-ish glow\n"
                    "right at the end of the path.\n"
                    "This way gives you a feeling of home.\n",
     "interaction": "\nYou find yourself at a junction.\n"
                    "The left path continues to what appears\n"
                    "to be a blank wall in the distance,\n"
                    "however, that way gives you a sense of excitement.\n"
                    "The right stretches farther than you can see,\n"
                    "but you can barely make out a blue-ish glow\n"
                    "right at the end of the path.\n"
                    "This way gives you a feeling of home.\n",
     "monster_presence": 0,
     "monster_class": "",
     "direction_choices": {
         "Left": 7,
         "Right": 6
     }},
    {"progress_text": "\nYou decide to take the right branch,\n"
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
                      "and you realise you will not be returning that way.\n",
     "description": "\nYou are standing just inside the doorway,\n"
                    "at the end of what appears to be a stone bridge.\n"
                    "The room appears square,\n"
                    "and you have entered at one of the corners.\n"
                    "Glancing upwards, the room doesn't"
                    " appear to have a ceiling,\n"
                    "just a darkness stretching infinitely to the heavens.\n"
                    "Similarly, peeking cautiously over"
                    " the edge of the 'bridge'\n"
                    "shows a dark chasm reaching down"
                    " into the bowels of the earth.\n"
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
    {"progress_text": "\nYou decide to take the left path,\n"
                      "and eventually you come to a right corner,\n"
                      "around which you can feel a very slight breeze.\n"
                      "You continue onwards and approach the next room,\n"
                      "the light of which is shining brightly.\n"
                      "Before you enter you scan the room for threats\n"
                      "but see nothing...\n"
                      "You cautiously enter...\n",
     "description": "You are standing in a brightly lit circular room,\n"
                    "smaller than any so far.\n"
                    "To the right of the room, not visible from the hallway,\n"
                    "is a small waterfall, flowing into a basin.\n"
                    "There's a small wooden cup"
                    " sitting on the side of the basin,\n"
                    "and a plaque that reads:\n"
                    "****************************************\n"
                    "REST WEARY ADVENTURER AND TAKE A DRINK\n"
                    "FOR THE NEXT ROOM WILL PUSH YOU TO THE BRINK\n"
                    "****************************************\n",
     "interaction": "\nYou drink a cup of water from the fountain.\n"
                    "It's cool and refreshing and\n"
                    "you feel yourself revitalised.\n"
                    "Good thing it's not poison or somethings.",
     "monster_presence": 0,
     "direction_choices": {
         "Forward": 8
     }},
    {"progress_text": "\nYou exit the room and enter the corridor beyond.\n"
                      "Similar to the entrance chamber,\n"
                      "this corridor is lined with statues.\n"
                      "As you make your way to the unusually\n"
                      "large doorway ahead, you begin to feel like\n"
                      "you have an honour guard of stone soldiers.\n"
                      "As you near the door you can see a large lump\n"
                      "lying in the middle of the floor,\n"
                      "and the smell that assails your nostrils\n"
                      "is nothing short of noxious.\n"
                      "You stand and gather your courage a moment,\n"
                      "before gritting your teeth, and entering.\n"
                      "The moment you enter the room\n"
                      "the lump begins to stir...\n"
                      "You don't need to guess what this creature is,\n"
                      "as it stands up and faces you it becomes\n"
                      "immediately clear you're facing an Ogre.\n",
     "description": "You're standing in a gargantuan square room.\n"
                    "It's made from the same stone as this entire dungeon\n"
                    "but it's the brightest room so far.\n"
                    "Apart from its stinky occupant\n"
                    "it seems rather unremarkable...\n"
                    "Well, except for the large chest at the very\n"
                    "far end of the room that is...",
     "interaction": "You ask the ogre how it is today.\n"
                    "It doesn't reply.\n",
     "monster_presence": 1,
     "monster_class": "Ogre",
     "monster_hp": 70,
     "monster_attack": 20,
     "direction_choices": {
         "Home": 9
     }}
]


class Player():
    """
    Main player class. Sets name, player class, hp, and attack.
    """
    def __init__(self, player_name, player_class, health_points, attack):
        self.player_name = player_name
        self.player_class = player_class
        self.health_points = health_points
        self.attack = attack


class Monster():
    """
    Main monster class. Sets monster class, hp, and attack.
    """
    def __init__(self, monster_class, health_points, attack):
        self.monster_class = monster_class
        self.health_points = health_points
        self.attack = attack


class Room():
    """
    Main room class, sets room_id and monster_presence
    """
    def __init__(self, room_id, monster_presence):
        self.room_id = room_id
        self.monster_presence = monster_presence


def start():
    """
    Starts game and builds player character
    """
    player_name = input("\nPlease enter your name: ")

    print("\nPlease choose a class:")

    player_classes = ["Archer", "Warrior", "Wizard"]
    player_class = enquiries.choose("", player_classes)

    if player_class == 'Warrior':
        health_points = random.randint(90, 100)
        attack = random.randint(15, 20)
    elif player_class == 'Wizard':
        health_points = random.randint(70, 80)
        attack = random.randint(25, 30)
    else:
        health_points = random.randint(80, 90)
        attack = random.randint(20, 25)

    player = Player(player_name, player_class, health_points, attack)

    current_room = 0

    time.sleep(0.5)
    print("\n****************************************"
          f"\nWelcome {player_name}!\n"
          f"You are playing as a {player_class}\n"
          f"Your Attack power is {player.attack}\n"
          f"And you have {player.health_points} Health Points\n"
          "****************************************\n")
    time.sleep(0.5)
    print("\nEver since you were old enough to\n"
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

    prompt_user(current_room, player)


def prompt_user(current_room, player):
    """
    Prompts user to select a command and progresses game
    """
    print(f"\nWhat would you like to do {player.player_name}?\n")

    player_choices = ["Continue", "Inspect", "Attack", "Interact", "Flee"]
    choice = enquiries.choose("", player_choices)

    if choice == "Continue":
        if current_room == 6:
            print("\nThe way back is sealed\n"
                  "and the room has no other exit.\n"
                  "Perhaps a risk must be taken...")
            prompt_user(current_room, player)
        elif current_room == 8 and room_list[
                current_room]["monster_presence"] == 0:
            print("\nWow, nice work!\n"
                  "First job as an Adventurer done and dusted.\n"
                  "You step past the dead ogre,\n"
                  "empty that lovely treasure chest\n"
                  "of all its goodies and decide it's time to skedaddle...\n"
                  "And as you're walking back through the dungeon,\n"
                  "your thoughts are already turning to your next job.\n"
                  "Onward Adventurer!")
        elif room_list[current_room]["monster_presence"] == 0:
            time.sleep(1)
            direction = enquiries.choose(
                "Which way will you go?\n",
                room_list[current_room]["direction_choices"])
            current_room = room_list[current_room].get(
                "direction_choices").get(direction)
            run_game(current_room, player)
        else:
            print("\nYou must defeat the monster(s) to proceed")
            prompt_user(current_room, player)
    elif choice == "Inspect":
        inspect_room(current_room, player)
    elif choice == "Attack":
        run_battle(current_room, player)
    elif choice == "Interact":
        player_interact(current_room, player)
    else:
        abort_game()


def run_game(current_room, player):
    """
    Moves players through game while giving brief description,
    then prompts for each 'room'
    """
    time.sleep(1)
    if current_room == 2 or current_room == 4:
        print(room_list[current_room]["progress_text"])
        abort_game()
    else:
        print(room_list[current_room]["progress_text"])
        prompt_user(current_room, player)


def inspect_room(current_room, player):
    """
    When user selects 'Inspect' prints a brief description
    of the current room, then prompts the player once more.
    Description is different for each room
    """
    print("\nYou inspect your surroundings...\n")

    time.sleep(1)
    print(room_list[current_room]["description"])
    prompt_user(current_room, player)


def run_battle(current_room, player):
    """
    When user selects 'Attack' option, initiates a 'battle' between
    player and monster.
    """
    time.sleep(1)

    for monster in range(room_list[current_room]["monster_presence"]):
        monster = Monster(
            room_list[current_room]["monster_class"],
            room_list[current_room]["monster_hp"],
            room_list[current_room]["monster_attack"])

    if room_list[current_room]["monster_presence"] == 0:

        print("\nI know you're eager Adventurer...\n"
              "but there's nothing to fight...\n"
              "except perhaps your own inner demons?")
        prompt_user(current_room, player)
    else:

        print(f"\nYou are fighting a {monster.monster_class}!")

        full_hp = player.health_points

        while monster.health_points > 0 and player.health_points > 0:

            attack_modifier = random.uniform(0.8, 1.2)
            monster_roll = round(monster.attack * attack_modifier)
            player_roll = round(player.attack * attack_modifier)

            time.sleep(0.5)
            print(f"\nThe {monster.monster_class} attacks"
                  f" for {monster_roll} points of damage!")
            player.health_points = player.health_points - monster_roll
            print(f"\nYou have {player.health_points} HP left")
            print(f"\n{player.player_name} attacks for"
                  f" {player_roll} points of damage")
            monster.health_points = monster.health_points - player_roll
            print(f"\nThe {monster.monster_class} has"
                  f" {monster.health_points} HP left")
        else:
            if player.health_points <= 0:
                print("\nOh no...\n"
                      "You died...\n"
                      "That was highly unexpected.\n"
                      "But then again everyone gets unlucky.\n")
                abort_game()
            else:
                print(f"\nYou defeated the {monster.monster_class}!"
                      f"\nCongratulations {player.player_name}!")

                print("\nWhew...\n"
                      "That was tough.\n"
                      "But you came prepared!\n"
                      "You chug a health potion,\n"
                      "and feel 100% again!\n")

                player.health_points = full_hp

                print(f"HP = {player.health_points}")

                room_list[current_room]["monster_presence"] -= 1
                prompt_user(current_room, player)


def player_interact(current_room, player):
    """
    Allows player to interact with environment when possible to do so
    """
    if current_room == 6:
        print(room_list[current_room]["interaction"])
        current_room = 0
        prompt_user(current_room, player)
    else:
        time.sleep(1)
        print(room_list[current_room]["interaction"])
        prompt_user(current_room, player)


def abort_game():
    """
    Ends game on user prompt or 'death' room
    """
    print("\nWell that's a pity :( Bye Bye\n"
          "If you'd like to have another go\n"
          "just click 'Run Program' ^")


start()