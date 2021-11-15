def start():
    """
    Starts game and prompts player for name
    """
    print("Welcome Adventurer!\n")
    print("What is your name?\n")
    name = input("My name is: ")
    print(f"\nWelcome {name}.\n")
    start_prompt = input("Are you ready to begin? y/n ").lower()

    if start_prompt == "y":
        play_game()
    elif start_prompt == "n":
        abort_game()
    else:
        print("Please input either 'y' or 'n'")


def play_game():
    print("Letsa go!")


def abort_game():
    print("k bye")


start()