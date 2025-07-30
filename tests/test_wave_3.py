from app.game import get_win_percentage, format_guess_stats

# --------------------------test get_win_percentage------------------------------------

def test_get_win_percentage_returns_int():
    # Arrange
    wins = 1
    plays = 15
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert type(result) == int


def test_get_win_percentage_no_games_returns_zero():
    # Arrange
    wins = 0
    plays = 0
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert result == 0


def test_get_win_percentage_no_wins_returns_zero():
    # Arrange
    wins = 0
    plays = 5

    # Act
    result = get_win_percentage(wins, plays)

    # Assert
    assert result == 0


def test_get_win_percentage_even_percentage():
    # Arrange
    wins = 3
    plays = 4
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert result == 75


def test_get_win_percentage_rounds_down():
    # Arrange
    wins = 1
    plays = 15
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert result == 6

def test_get_win_percentage_all_wins():
    # Ensures the function works for the maximum possible win rate, catching bugs that miss full matches.
    # Arrange
    wins = 10
    plays = 10

    # Act
    result = get_win_percentage(wins, plays)

    # Assert
    assert result == 100

def test_get_win_percentage_large_numbers():
    # Verifies the function works for large values, preventing bugs with integer math.
    # Arrange
    wins = 1000000
    plays = 2000000

    # Act
    result = get_win_percentage(wins, plays)

    # Assert
    assert result == 50

# --------------------------test format_guess_stats------------------------------------

def test_format_guess_stats_no_games():
    # Arrange
    guess_stats = {}
    
    # Act
    result = format_guess_stats(guess_stats)
    
    # Assert
    assert len(result) == 8
    for s in result:
        assert s == ''


def test_format_guess_stats_one_pair():
    # Arrange
    guess_stats = {1: 4}
    
    # Act
    result = format_guess_stats(guess_stats)
    
    # Assert
    assert len(result) == 8

    # Check first entry is 4 Xs
    assert len(result[0]) == 4
    assert type(result[0]) == str
    for char in result[0]:
        assert char == 'X'

    # Check following entries are empty
    for index in range(1, 8):
        assert result[index] == ''


def test_format_guess_stats_all_pairs():
    # Arrange
    guess_stats = {
        1: 4,
        2: 3,
        3: 4,
        4: 2,
        5: 6,
        6: 1,
        7: 1,
        8: 3
    }
    
    # Act
    result = format_guess_stats(guess_stats)
    
    # Assert
    assert len(result) == 8

    assert len(result[0]) == 4
    assert result[0] == 'XXXX'

    assert len(result[1]) == 3
    assert result[1] == 'XXX'

    assert len(result[2]) == 4
    assert result[2] == 'XXXX'
    
    assert len(result[3]) == 2
    assert result[3] == 'XX'

    assert len(result[4]) == 6
    assert result[4] == 'XXXXXX'

    assert len(result[5]) == 1
    assert result[5] == 'X'

    assert len(result[6]) == 1
    assert result[6] == 'X'

    assert len(result[7]) == 3
    assert result[7] == 'XXX'

def test_format_guess_stats_missing_middle_keys():
    # Ensures the function handles missing keys in the middle, preventing bugs in mapping and output formatting.
    # Arrange
    guess_stats = {1: 2, 3: 1, 8: 5}

    # Act
    result = format_guess_stats(guess_stats)

    # Assert
    assert result[0] == 'XX'
    assert result[1] == ''
    assert result[2] == 'X'
    for i in range(3, 7):
        assert result[i] == ''
    assert result[7] == 'XXXXX'

def test_format_guess_stats_zero_wins_for_some_keys():
    # Verifies that zero values are handled as empty strings, preventing bugs in output formatting.
    # Arrange
    guess_stats = {2: 0, 5: 3}

    # Act
    result = format_guess_stats(guess_stats)

    # Assert
    assert result[0] == ''
    assert result[1] == ''
    for i in range(2, 4):
        assert result[i] == ''
    assert result[4] == 'XXX'
    for i in range(5, 8):
        assert result[i] == ''

def test_format_guess_stats_large_number_of_wins():
    # Ensures the function handles large values, preventing bugs with string length and output formatting.
    # Arrange
    guess_stats = {4: 100}

    # Act
    result = format_guess_stats(guess_stats)

    # Assert
    assert result[3] == 'X' * 100
    for i in range(8):
        if i != 3:
            assert result[i] == ''

def test_format_guess_stats_non_sequential_keys():
    # Verifies that keys out of order are placed in the correct output positions, preventing mapping bugs.
    # Arrange
    guess_stats = {8: 2, 1: 1, 5: 3}

    # Act
    result = format_guess_stats(guess_stats)

    # Assert
    assert result[0] == 'X'
    assert result[4] == 'XXX'
    assert result[7] == 'XX'
    for i in range(8):
        if i not in [0, 4, 7]:
            assert result[i] == ''
