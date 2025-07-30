# Mastermind with Copilot

## Goals

Our goals for this lesson are to:
- Write code with Copilot to manipulate and process data in lists, strings, and dictionaries
- Write code to a specification while using a coding assistant
- Continue to practice reading tests

## Mastermind Game Details

Mastermind is a game in which one player, the codemaker, generates a code consisting of four colored pegs. 
- Each peg can be one of six colors: red, orange, yellow, green, blue, or purple.
- The second player, the codebreaker, attempts to guess the codemaker's code by submitting their own series of four colored pegs. 

After each guess by the codebreaker, the codemaker provides the codebreaker with two numbers:
1. The number of pegs that are both the correct color and in the correct position
2. The number of pegs that are the correct color but in the wrong position

The codebreaker continues to submit guesses and receive feedback until they correctly guess the code or run out of tries. The aim of the game is to guess the codemaker's code in the least number of guesses.

In this version of Mastermind: 
- We will use the letters `['R', "O" 'Y', 'G', 'B', 'P']` to represent pegs colored red, orange, yellow, green, blue, and purple respectively.
- We will limit the maximum number of guesses to 8. 
    - If the codebreaker does not correctly guess the code within 8 guesses, they lose the game.
- We will create a randomly generated code for the codebreaker to guess. Our game itself will act as the codemaker.

## Project Set Up

The goal of this project is to write code in `game.py` and `mastermind.py` so each of the functions and files meet the requirements outlined in the Project Directions below.

### One Time Project Set up

1. Create a fork of this repository
2. Clone down the fork 
3. Create a virtual environment
4. Use `pip` to install the packages in `requirements.txt`

## Details on Testing

Throughout the development of our project, we will use a combination of unit testing and play testing to help verify the correctness of our program. Unit testing is where we test small modules of our code individually. Play testing is where we run our program and play versions of our game as we develop it in order to discover and fix any flaws or bugs.

- For Waves 1-3, we will primarily use unit tests to guide development. 
- For Wave 4, we will use play testing to guide our development. 

Optionally, you may find it useful to write your own unit tests to further test Waves 1-3 or your game loop in Wave 4. You may also find it helpful to do play testing of the functions you develop in Waves 1-3 by importing and calling them in `main.py` or `mastermind.py`'s `mastermind` function.

Before beginning the project, try to run the unit tests. At this point, unit test discovery should fail since we do not have placeholders for any of the functions in `game.py`

## Project Directions

### Get Familiar

Take time to read through the Wave implementation requirements and the tests for each Wave. 
- Write down your questions, and spend some time going through your understanding of the requirements and tests. 
- Make sure you can run the tests and see them fail.

### Wave 1: Game Setup, Validate Guesses, and Game End Conditions

#### Implement `generate_code`

The first step in setting up a new game is to generate a code of 4 colors (represented as letters) for the user to guess. To do so, implement the function `generate_code` in `game.py`. 

This function should have the following properties:
- No parameters
- Returns a list of length 4
- Each element in the list should be any of the following letters: R, O, Y, G, B, P

#### Implement `validate_guess`

Next, we need a way to check if a user's guess is of the correct length and only uses valid letters. To do so, implement the function called `validate_guess` in `game.py`. This function should have the following properties:

- Has one parameter
    - `guess` describes some input list
- Returns either `True` or `False`
    - Returns `True` 
        - if every element in `guess` one of the following letters: R, O, Y, G, B, P
        - the length of `guess` is 4 (the length of the generated code)
    - Returns `False` if not; 
        - if there is a letter in `input` that is not R, O, Y, G, B, or P 
        - if the length of `input` is not 4
- `validate_guess` should be case insensitive
    - Both the inputs `['R','Y','G','B']` and `['r','y','g','b']` should return `True`

**Examples**

| code | guess | output |
| :--: | :---: | :----: |
| ['R','P','Y','G'] | ['R','P','Y','G'] | True  |
| ['R','P','Y','G'] | ['R','O','Y','G'] | False |
| ['R','P','Y','G'] | ['R','p','Y','G'] | True  |
| ['R','P','Y','G'] | ['r','p','y','g'] | True  |
| ['R','P','Y','G'] | ['R','P','Y','G','B'] | False |

#### Implement `check_code_guessed`

Once a user has entered their guess, we need a method to check whether or not the round has been won.

Implement a function called `check_code_guessed` in `game.py`. This function should have the following properties:
- Has three parameters:
  - `guess`, which is a list of characters representing the user's guess
  - `code`, which is a list of characters representing the code the user is attempting to guess
- Returns `True` if the user has won the game 
    - `guess` and `code` are the same regardless of letter casing
- Returns `False` otherwise

**Examples**

| guess | code | output |
|:-----:|:----:| :----: |
| ['R','P','Y','G'] | ['R','P','Y','G'] | True |
| ['r','p','y','g'] | ['R','P','Y','G'] | True |
| ['R','P','Y','G'] | ['R','R','R','R'] | False |

### Wave 2: Provide User Feedback
Now we need to provide feedback to the user about their guess as defined by the Mastermind game. The goal is to provide the user with two numbers:
1. The number of pegs that are both the correct color and in the correct position
2. The number of pegs that are the correct color but in the wrong position

To do this, you will write three functions: `color_count`, `correct_pos_and_color`, and `generate_hint`.

#### Implement `color_count`

The first function to implement is `color_count` in `game.py`. This function should have the following properties:
- Takes in two parameters:
    - `guess`, which is a string of characters representing the user's guess
    - `code`, which is a string of characters representing the code the user is attempting to guess
- Returns an integer representing the number of pegs that are the correct color (aka letter), **regardless of whether they are in the correct position or not**
    - If no pegs are the correct color, `color_count` returns `0`
- A letter that appears more times in `guess` than it appears in `code` is counted the number of times it appears in `code`
- A letter that appears fewer times in `guess` than it appears in `code` is counted the number of times it appears in `guess`


**Examples**
|guess              | code              | output|
|:-----------------:|:-----------------:|:-----:|
|['R','P','Y','G']  |['G','Y','P','R']  | 4     |
|['R','P','Y','G']  |['R','Y','P','G']  | 4     |
|['R','R','R','B']  |['B','P','R','R']  | 3     |
|['R','R','P','P']  |['B','R','R','R']  | 2     |
|['R','P','Y','G']  |['O','O','O','O']  | 0     |

#### Implement `correct_pos_and_color`

The second function to implement is `correct_pos_and_color` in `game.py`. This function should have the following properties:
- Has two parameters:
    - `guess`, which is a list of characters representing the user's guess
    - `code`, which is a list of characters representing the code the user is attempting to guess
- Returns an integer representing the number of pegs in `guess` whose color (aka letter) is the same as the peg at the matching index in `code`
    - If no pegs in `guess` match both the color and index of those in `code`, `correct_pos_and_color` returns `0`

**Examples**

| guess | code | output |
| :---: | :--: |:------:|
| ['R','P','Y','G'] | ['R','P','Y','G'] | 4 |
| ['R','P','Y','G'] | ['G','Y','P','R'] | 0 |
| ['R','R','R','B'] | ['R','P','B','B'] | 2 |

#### Implement `generate_hint`

The final function to implement is `generate_hint` in `game.py`. This function should have the following properties:
- Has two parameters:
  - `guess`, which is a list of characters representing the user's guess
  - `code`, which is a list of characters representing the code the user is attempting to guess
  - Returns a tuple of two integers
    - the first integer is the number of pegs in `guess` that have the same color and position as the corresponding pegs in `code`
    - The second integer is the number of pegs in `guess` that are the correct color but in a different position than the pegs in `code`

**Examples**

| guess | code | output |
| :---: | :--: | :----: |
| ['R','P','Y','G'] | ['G','Y','P','R'] | 0, 4 |
| ['R','P','Y','G'] | ['R','Y','P','G'] | 2, 2 |
| ['R','R','R','B'] | ['B','P','R','R'] | 1, 2 |
| ['R','R','P','P'] | ['B','R','R','R'] | 1, 1 |
| ['R','P','Y','G'] | ['O','O','O','O'] | 0, 0 |

### Wave 3: Statistics

We also want to track statistics over multiple rounds and display those statistics at the end of each round. 

#### Implement `get_win_percentage`

To aid us in this, implement `get_win_percentage` which has the following properties:
- Has two parameters
    - `wins`, which is an integer representing the number of games the user has won
    - `plays`, which is an integer representing the total number of rounds the user has played in the session
- Returns an integer representing the percentage of rounds won over the current session
    - the win percentage should round down

**Examples**

| wins | plays | output|
|:----:|:-----:|:-----:|
| 0 | 0 | 0 |
| 0 | 4 | 0 |
| 3 | 4 | 75 |
| 1 | 15 | 6 |

#### Implement `format_guess_stats`

Next, implement the `format_guess_stats` function which has the following properties:
- Has one parameter:
    - `guess_stats`, a dictionary where `key` `i` is the number of guesses and the paired `value` is the number of games won in that amount of guesses
- Returns a list of length 8
    - Element at index `i` of the list is a string of _n_ `X`s, where _n_ is the number of rounds won in `i+1` guesses
    - If _n_ is 0, the string should be empty

**Examples**

| guess_stats | output |
| :---------: | :----: |
| {1: 1, 3:4, 5:1 } | ['X', '', 'XXXX', '', 'X', '','',''] | 
| {} | ['','','','','','','',''] |

### Wave 4: Game Loop

Using the functions built in previous waves, complete the `mastermind` function in `app/mastermind.py`. 
- Note that there are no tests to verify the correctness of your game loop. Instead use play testing and the example outputs provided below to guide your implementation.

The `mastermind` function should implement a game loop. The game loop is a loop that will keep the game running until the user wants to stop playing and defines the overall logic flow of the game. As part of our game loop, we will need to track the following data:
- `plays`, an integer representing the total number of rounds played
- `wins`, an integer representing the total number of rounds won
- `guess_stats`, a dictionary representing the number of rounds won in _n_ guesses 
    - Only rounds where the player won the game (total number of guesses was less than or equal to 8) are added to `guess_stats`
- `guesses`, an integer representing the number of guesses the user has made in the current round

Your game loop does not need to match the example output we provide below word for word, however it should contain these basic components:
1. Welcome message on program start
2. Prompt for user input and give feedback on how that user input compares to the secret code continuously until the user either
    - correctly guesses the code
    - exceeds 8 guesses
3. Winning message if the user correctly guesses the code in 8 guesses or under
4. Losing message if the user fails to correctly guess the code in 8 guesses or under
5. Print out of Session Statistics after a round finishes 
    - Number of rounds played
    - Win Percentage (what percentage of all rounds played were won)
    - Guess Distribution Graph:
        - How many of the rounds played were won with each possible number of guesses (1-8)
6. Option to play another round

**Examples**

The game loop should begin the program with a welcome message.
#### Example Welcome Message
```
Welcome to Mastermind!
```

The game loop should then generate a new code to guess and give the user directions on how to play the game.

#### Example Instructions
```
Generating a new code...
New code generated: ****
Guess the code! Each character in the code is one of the following letters: R, O, Y, G, B, P
```

The game loop should then prompt the user to input a guess.
#### Example User Prompt
```
Guess the code:
```
The game loop should take the user's input and print it out.

#### Example Guess Print Out
```
Assume
    user_input = RRRB
----------
Game Loop Output
    You guessed: RRRB
```

If the user did not correctly guess the secret code, we should also print out feedback about how many of the letters in their guess were the correct color and in the correct position and how many were the correct color but in the wrong position.

#### Example Guess Feedback
```
Assume 
    code = BPRR
    user_input = RRRB
------
Game Loop Output
    (1,2)
```

The game loop should continue to prompt the user for new guesses and provide corresponding feedback until they have correctly guessed the code or surpassed 8 guesses.
#### Example Feedback Loop
```
Assume 
    code = BPRR
------
Game Loop Output
    You guessed: RRRB
    (1,2)
    Guess the code: 
    You guessed: BRRR
    (3,0)
    Guess the code:
    You guessed: BRGR
    (2,1)
    Guess the code:
    ...
```

If the user correctly guesses the code at any point during the game, they have won the game. The game loop should stop prompting them for additional guesses and display a message congratulating them for winning the game.

```
Assume 
    code = BPRR
------
Game Loop Output
    You guessed: BPRR
    Congratulations! You guessed the secret code!
```

If the user has made 8 guesses and still has not correctly guessed the secret code, they have lost the game. The game loop should stop prompting them for additional guesses and display a lose message.
```
Assume 
    code = BPRR
------
Game Loop Output
    Guess the code:
    You guessed: RRRB
    (1,2)
    Guess the code: 
    You guessed: RRRB
    (1, 2)
    Guess the code:
    You guessed: RRRB
    (1, 2)
    Guess the code:
    You guessed: RRRB
    (1,2)
    Guess the code: 
    You guessed: RRRB
    (1, 2)
    Guess the code:
    You guessed: RRRB
    (1,2)
    Guess the code: 
    You guessed: RRRB
    (1, 2)
    Guess the code:
    You guessed: RRRB
    (1,2)
    You lost 😥 Better luck next time!
```
Regardless of whether the player wins or loses, once the round has finished, the game loop should print out statistics about the session so far. Statistics should include:
- Number of rounds played
- Win Percentage (what percentage of all rounds played were won)
- Guess Distribution Graph:
    - How many of the rounds played were won with each possible number of guesses (1-8)
#### Example Session Statistics
```
STATISTICS
Games Played: 10
Win %: 80
Guess Distribution:
1| X
2| 
3| XXX
4| 
5| 
6| XX
7| X
8| X 
```
Finally, after printing out the session statistics, the game loop should ask the user whether they would like to play again. If the user responds yes, a new round of the game should begin. Otherwise, the program should end.
#### Example Play Again Prompt
```
Should we play another round?
Enter y to replay, any other character to exit:
```



#### Example of a Full Game Loop
Note that lines marked #### denote user input and are not printed by the program as part of the game loop
```
Welcome to Mastermind!
Generating a new code...
New code generated: ****
Guess the code! Each character in the code is one of the following letters: R, O, Y, G, B, P
Guess the code: 
####user input: GRRY
You guessed: GRRY
Congratulations! You guessed the secret code!
STATISTICS
Games Played: 1
Win %: 100
Guess Distribution:
1| X
2| 
3| 
4| 
5| 
6| 
7| 
8| 
Should we play another round?
Enter y to replay, any other character to exit: 
####user input: y

Generating a new code...
New code generated: ****
Guess the code! Each character in the code is one of the following letters: R, O, Y, G, B, P
Guess the code: 
####user input: RRRB
You guessed: RRRB
(1,2)
Guess the code: 
####user input: BPRR
You guessed: BPRR
Congratulations! You guessed the secret code!
STATISTICS
Games Played: 2
Win %: 100
Guess Distribution:
1| X
2| X
3| 
4| 
5| 
6| 
7| 
8| 
Should we play another round?
Enter y to replay, any other character to exit: 
####user input: y

Generating a new code...
New code generated: ****
Guess the code! Each character in the code is one of the following letters: R, O, Y, G, B, P
Guess the code: 
####user input: RRRR
You guessed: RRRR
(1,2)
Guess the code: 
####user input: RRRR
You guessed: RRRR
(1,2)
Guess the code: 
####user input: RRRR
You guessed: RRRR
(1,2)
Guess the code: 
####user input: RRRR
You guessed: RRRR
(1,2)
Guess the code: 
####user input: RRRR
You guessed: RRRR
(1,2)
Guess the code: 
####user input: RRRR
You guessed: RRRR
(1,2)
Guess the code: 
####user input: RRRR
You guessed: RRRR
(1,2)
Guess the code: 
####user input: RRRR
You guessed: RRRR
(1,2)
You lost 😥 Better luck next time!
STATISTICS
Games Played: 3
Win %: 66
Guess Distribution:
1| X
2| X
3| 
4| 
5| 
6| 
7| 
8| 
Should we play another round?
Enter y to replay, any other character to exit: 
####user input: n
```
