from random import randint
from game_data import data
from art import logo, vs


def gameplay() -> None:
    """Runs Higher Lower Game.
    The purpose of the game is for the user to guess which of the two presented options
    has more Instagram Followers."""
    print(logo)
    score = 0
    played_entries = []
    option_one, option_two = None, None
    while True:
        if not score:
            option_one = get_random_entry(data, played_entries)
        option_two = get_random_entry(data, played_entries)
        print(f"Compare A: {option_one['name']}, {option_one['description']}, {option_one['country']}.")
        print(vs)
        print(f"Against B: {option_two['name']}, {option_two['description']}, {option_two['country']}.")
        while True:
            guess = input("Who do you think has more followers? Please enter 'A' or 'B': ").lower()
            if guess not in ("a", "b"):
                print("That's not a valid guess. Please try again.")
            else:
                break
        if option_one["follower_count"] > option_two["follower_count"]:
            correct_option, correct_answer = option_one, 'a'
        else:
            correct_option, correct_answer = option_two, 'b'
        if guess == correct_answer:
            score += 1
            option_one = correct_option
            if score == len(data):
                print("Congratulations. You beat the game! Be very proud of yourself.")
                exit()
            else:
                print(f"\nThat's right! Current score: {score}")
        else:
            print(f"Sorry, wrong answer! Final score: {score}.")
            while True:
                to_continue = input(f"Would you like to start a new game? "
                                    f"Enter 's' to start a new game, or 'e' to exit the program: ")
                if to_continue == 's':
                    score = 0
                    played_entries = []
                    print(logo)
                    print("\nLet's go again!")
                    break
                elif to_continue == 'e':
                    print("\nThank you for playing. Goodbye!")
                    exit()
                else:
                    print("That's not a valid input. Please try again!")


def get_random_entry(available_entries: list, played_entries: list) -> dict:
    """Takes in two lists of dictionary data, return random entry
    from the first list not present in the second list
    """
    random_entry = available_entries[randint(0, len(available_entries) - 1)]
    while random_entry in played_entries:
        random_entry = available_entries[randint(0, len(available_entries) - 1)]
    played_entries.append(random_entry)
    return random_entry


gameplay()
