from app.game import color_count, correct_pos_and_color, generate_hint

# --------------------------test color_count------------------------------------
def test_color_count_returns_int():
    # Arrange
    guess = ['R', 'R', 'G', 'B']
    code = ['R', 'G', 'B', 'P']

    # Act
    result = color_count(guess, code)

    # Assert
    assert type(result) == int


def test_color_count_two_matching():
    # Arrange
    guess = ['R', 'O', 'G', 'B']
    code = ['R', 'O', 'P', 'P']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 2


def test_color_count_order_does_not_matter():
    # Arrange
    guess = ['R', 'O', 'G', 'B']
    code = ['P', 'P', 'R', 'O']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 2


def test_color_count_letter_not_double_counted():
    # Arrange
    guess = ['R', 'R', 'G', 'B']
    code = ['R', 'P', 'P', 'P']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 1


def test_color_count_duplicates_counted_if_echoed():
    # Arrange
    guess = ['R', 'R', 'G', 'P']
    code = ['R', 'R', 'O', 'B']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 2


def test_color_count_no_match_returns_zero():
    # Arrange
    guess = ['R', 'B', 'O', 'O']
    code = ['P', 'P', 'P', 'P']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 0

def test_color_count_all_colors_match_with_duplicates():
    # Ensures the function works for the maximum possible matches with duplicates, catching bugs that miss full matches.
    # Arrange
    guess = ['R', 'R', 'G', 'G']
    code = ['R', 'R', 'G', 'G']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 4

def test_color_count_guess_has_more_of_color():
    # Prevents over-counting when guess has more instances of a color than code, catching bugs in match limits.
    # Arrange
    guess = ['R', 'R', 'R', 'G']
    code = ['R', 'G', 'B', 'P']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 2

def test_color_count_code_has_more_of_color():
    # Prevents over-counting when code has more instances of a color than guess, catching bugs in match limits.
    # Arrange
    guess = ['R', 'G', 'B', 'P']
    code = ['R', 'R', 'R', 'G']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 2

def test_color_count_all_colors_match_wrong_positions():
    # Ensures color matching logic is correct even when all matches are in wrong positions, catching bugs in color-only logic.
    # Arrange
    guess = ['R', 'G', 'B', 'Y']
    code = ['Y', 'B', 'G', 'R']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 4

#--------------------------test correct_pos_and_color------------------------------------

def test_correct_pos_and_color_returns_int():
    # Arrange
    guess = ['R', 'B', 'B', 'B']
    code = ['O', 'O', 'O', 'O']

    # Act
    result = correct_pos_and_color(guess, code)

    # Assert
    assert type(result) == int


def test_correct_pos_and_color_two_match():
    # Arrange
    guess = ['R', 'B', 'O', 'P']
    code = ['R', 'B', 'G', 'G']

    # Act
    result = correct_pos_and_color(guess, code)

    # Assert
    assert result == 2


def test_correct_color_but_not_pos_returns_zero():
    # Arrange
    guess = ['R', 'B', 'O', 'P']
    code = ['O', 'P', 'R', 'B']

    # Act
    result = correct_pos_and_color(guess, code)

    # Assert
    assert result == 0


def test_correct_color_and_pos_dups_not_double_counted():
    # Arrange
    guess = ['R', 'B', 'O', 'R']
    code = ['R', 'P', 'P', 'P']

    # Act
    result = correct_pos_and_color(guess, code)

    # Assert
    assert result == 1


def test_correct_pos_and_color_no_match_returns_zero():
    # Arrange
    guess = ['R', 'B', 'P', 'P']
    code = ['O', 'O', 'O', 'O']

    # Act
    result = correct_pos_and_color(guess, code)

    # Assert
    assert result == 0

# Additional coverage tests for correct_pos_and_color
def test_correct_pos_and_color_all_positions_match():
    # Ensures the function works for the maximum possible matches, catching bugs that miss full matches.
    # Arrange
    guess = ['R', 'O', 'Y', 'G']
    code = ['R', 'O', 'Y', 'G']

    # Act
    result = correct_pos_and_color(guess, code)

    # Assert
    assert result == 4

def test_correct_pos_and_color_alternating_matches():
    # Detects off-by-one or index errors by verifying matches at non-adjacent positions.
    # Arrange
    guess = ['R', 'O', 'Y', 'G']
    code = ['R', 'P', 'Y', 'B']

    # Act
    result = correct_pos_and_color(guess, code)

    # Assert
    assert result == 2  # positions 0 and 2 match

def test_correct_pos_and_color_all_duplicates_all_match():
    # Verifies that repeated values are handled correctly, preventing bugs with duplicate logic.
    # Arrange
    guess = ['R', 'R', 'R', 'R']
    code = ['R', 'R', 'R', 'R']

    # Act
    result = correct_pos_and_color(guess, code)

    # Assert
    assert result == 4

#--------------------test generate_hint()-------------------------------------

def test_generate_hint_matching_codes():
    # Arrange
    guess = ['R', 'B', 'P', 'P']
    code = ['R', 'B', 'P', 'P']

    # Act
    result = generate_hint(guess, code)

    # Assert
    assert result == (4, 0)


def test_generate_hint_mixed_guess():
    # Arrange
    guess = ['R', 'B', 'O', 'P']
    code = ['R', 'Y', 'B', 'P']

    # Act
    result = generate_hint(guess, code)

    # Assert
    assert result == (2, 1)


def test_generate_hint_completely_incorrect():
    # Arrange
    guess = ['P', 'P', 'P', 'P']
    code = ['R', 'R', 'R', 'R']

    # Act
    result = generate_hint(guess, code)

    # Assert
    assert result == (0, 0)


# Additional coverage tests for generate_hint
def test_generate_hint_all_colors_wrong_positions():
    # Ensures the function correctly handles cases where all colors are present but none are in the correct position, catching bugs in color-only logic.
    # Arrange
    guess = ['R', 'G', 'B', 'Y']
    code = ['Y', 'B', 'G', 'R']

    # Act
    result = generate_hint(guess, code)

    # Assert
    assert result == (0, 4)

def test_generate_hint_some_positions_some_colors_with_duplicates():
    # Verifies correct handling of duplicates and mixed matches, preventing bugs in duplicate logic and match separation.
    # Arrange
    guess = ['R', 'R', 'G', 'B']
    code = ['R', 'G', 'R', 'B']

    # Act
    result = generate_hint(guess, code)

    # Assert
    assert result == (2, 2)

def test_generate_hint_no_positions_some_colors():
    # Ensures color-only matches are counted when no positions match, preventing bugs in color-only logic.
    # Arrange
    guess = ['R', 'G', 'B', 'Y']
    code = ['G', 'R', 'Y', 'B']

    # Act
    result = generate_hint(guess, code)

    # Assert
    assert result == (0, 4)

def test_generate_hint_some_positions_no_other_colors():
    # Prevents over-counting color-only matches when all matches are positional, catching bugs in match separation.
    # Arrange
    guess = ['R', 'G', 'B', 'Y']
    code = ['R', 'G', 'B', 'O']

    # Act
    result = generate_hint(guess, code)

    # Assert
    assert result == (3, 0)


