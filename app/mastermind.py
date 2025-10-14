from .game import generate_code, validate_guess, check_code_guessed, generate_hint, get_win_percentage, format_guess_stats, normalize_code

# Wave 4

PLAYS_KEY = 'plays'
WINS_KEY = 'wins'
GUESS_STATS_KEY = 'guess_stats'

def init_stats():
    """
    Returns a new stats dictionary for tracking game session.
    """
    return {PLAYS_KEY: 0, WINS_KEY: 0, GUESS_STATS_KEY: {}}

def update_stats(stats, won, guesses):
    """
    Updates the stats dictionary after a round.
    stats: dict with keys 'plays', 'wins', 'guess_stats'
    won: bool, whether the player won
    guesses: int, number of guesses used in the round
    """
    stats[PLAYS_KEY] += 1
    if won:
        stats[WINS_KEY] += 1
        stats[GUESS_STATS_KEY][guesses] = stats[GUESS_STATS_KEY].get(guesses, 0) + 1

def print_stats(stats):
    """
    Prints the session statistics after a round.
    """
    print("STATISTICS")
    print(f"Games Played: {stats[PLAYS_KEY]}")
    print(f"Win %: {get_win_percentage(stats[WINS_KEY], stats[PLAYS_KEY])}")
    print("Guess Distribution:")
    stats_list = format_guess_stats(stats[GUESS_STATS_KEY])
    for i, stat in enumerate(stats_list, 1):
        print(f"{i}| {stat}")

def play_round(MAX_GUESSES=8):
    """
    Plays a single round of Mastermind. Returns (won, guesses).
    """
    print("Generating a new code...")
    code = generate_code()
    print("New code generated: ****")
    print("Guess the code! Each character in the code is one of the following letters: R, O, Y, G, B, P")
    guesses = 0
    won = False

    while guesses < MAX_GUESSES:
        guess_input = input("Guess the code: ")
        guess = normalize_code(guess_input)
        if not validate_guess(guess):
            print("Invalid guess. Please enter 4 valid letters (R, O, Y, G, B, P).")
            continue

        guesses += 1
        print(f"You guessed: {''.join(guess)}")

        if check_code_guessed(guess, code):
            print("Congratulations! You guessed the secret code!")
            won = True
            break
        else:
            hint = generate_hint(guess, code)
            print(hint)

    if not won:
        print("You lost 😥 Better luck next time!")
    return won, guesses

def mastermind():
    MAX_GUESSES = 8
    stats = init_stats()
    replay = 'y'

    print("Welcome to Mastermind!")

    while replay == 'y':
        won, guesses = play_round(MAX_GUESSES)
        update_stats(stats, won, guesses)
        print_stats(stats)

        print("Should we play another round?")
        replay = input("Enter y to replay, any other character to exit: ").strip().casefold()