import random


# Wave 1
VALID_LETTERS = {'R', 'O', 'Y', 'G', 'B', 'P'}

def generate_code():
    # Generate a code of 4 random letters from VALID_LETTERS using a list comprehension
    letters_list = list(VALID_LETTERS)
    return [random.choice(letters_list) for _ in range(4)]


def validate_guess(guess):
    # Exit early if guess is not exactly 4 elements long
    if len(guess) != 4:
        return False
    
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = normalize_code(guess)

    # Return False if we find an invalid element of guess
    for letter in uppercased_guess:
        if letter not in VALID_LETTERS:
            return False
        
    return True


def check_code_guessed(guess, code):
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = normalize_code(guess)
    # Check if the guess and code are identical (win condition)
    return code == uppercased_guess


def normalize_code(code):
    """
    Normalizes the casing for a code by converting 
    the list of characters to uppercase.
    """    
    return [str(letter).upper() for letter in code]


# Wave 2
# Add your Wave 2 functions here

def generate_hint(guess, code):
    """
    Returns a tuple:
        (number of correct positions, number of correct colors in wrong positions)
    Assumes guess and code are normalized lists of length 4.
    """
    correct_positions = correct_pos_and_color(guess, code)
    total_correct_colors = color_count(guess, code)
    color_only = total_correct_colors - correct_positions
    return (correct_positions, color_only)


def color_count(guess, code):
    """
    Returns the number of colors in guess that are correct, regardless of position.
    Both guess and code are lists of length 4, containing valid color letters.
    """
    from collections import Counter
    # Assume guess and code are already normalized (uppercase, valid colors)
    intersection = Counter(guess) & Counter(code)
    count = intersection.total()
    return count


def correct_pos_and_color(guess, code):
    """
    Returns the number of positions where guess and code match exactly.
    Assumes guess and code are normalized lists of length 4.
    """
    return sum(g == c for g, c in zip(guess, code))


# Wave 3

def get_win_percentage(wins, plays):
    """
    Returns the integer percentage (rounded down) of games won out of games played.
    If no games have been played, returns 0.

    Note: If wins exceeds plays, this function does not guard against it and will return a percentage greater than 100. Input validation should prevent this if undesired.
    """
    if plays == 0:
        return 0
    return (wins * 100) // plays

MAX_GUESSES = 8

def format_guess_stats(guess_stats):
    """
    Returns a list of MAX_GUESSES strings. Each string contains Xs representing the number of games won in n guesses (offset by one).
    If no games were won for a guess count, the string is empty.
    """
    result = []
    for position in range(MAX_GUESSES):
        guess_count = position + 1  # guess_stats keys are 1-based
        wins = guess_stats.get(guess_count, 0)
        result.append('X' * wins if wins > 0 else '')
    return result

