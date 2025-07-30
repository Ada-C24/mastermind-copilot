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


# Wave 3
# Add your Wave 3 functions here
