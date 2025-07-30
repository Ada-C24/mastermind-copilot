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

    assert result == 1


def test_color_count_duplicates_counted_if_echoed():
    # Arrange
    guess = ['R', 'R', 'G', 'P']
    code = ['R', 'R', 'O', 'B']

    # Act
    result = color_count(guess, code)

    assert result == 2


def test_color_count_no_match_returns_zero():
    # Arrange
    guess = ['R', 'B', 'O', 'O']
    code = ['P', 'P', 'P', 'P']

    # Act
    result = color_count(guess, code)

    # Assert
    assert result == 0

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