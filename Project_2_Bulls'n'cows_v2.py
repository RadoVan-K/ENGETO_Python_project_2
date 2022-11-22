# Druhý projekt do Engeto Online Python Akademie - Bulls'n'cows

# author: Radovan Krejčíř
# email: krejcir.rad@gmail.com
# discord: Radovan K.#3299
# GitHub: RadoVan-K


# imported libraries

import random

# global variables

head = '''

Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number. But be careful, you only have 20 guesses!
-----------------------------------------------
'''

line = '-----------------------------------------------'
game_on = True
players_choice = ''
lives = 20


# function to create a random 4-digit number (not starting with 0)

def give_number(length: int) -> str:
    """Returns a numerical string with its length as a parameter. 0 excluded on the first position. """

    number_range = range(1, length + 1)
    number = ''

    for digit in number_range:
        if digit == 1:
            digit = str(random.randrange(1, 10))
        else:
            digit = str(random.randrange(10))
        number = number + digit

    return number


# function to identify "bulls" in the user's guess

def check_bulls(number_to_guess: str, guess: str) -> list:
    """
    Identifies positions with identical symbol within two strings of the same length ("number_to_guess", "guess") and
    returns a list with their indexes (in reversed order).
    """

    bulls_index = []
    number_of_digits = range(1, 5)

    for i in number_of_digits:
        if guess[i - 1] == number_to_guess[i - 1]:
            bulls_index.append(i)

    bulls_index.reverse()

    return bulls_index


# function to subtract "bulls" from both, number-to-guess and user's guess

def subtract_bulls(number_to_subtract: str, bulls_index: list) -> list:
    """
    Converts a numerical string ("number to subtract") to a list
    and deletes values on indexes specified by the second parameter "bulls_index".
    """

    subtracted = list(number_to_subtract)

    for i in bulls_index:
        subtracted.pop(i - 1)

    return subtracted


# function to identify "cows" in the user's guess

def check_cows(number_nobulls: list, guess_nobulls: list) -> list:
    """
    Identifies values shared between two lists (not index dependent) and returns a list with their indexes.
    """

    cows_index = []

    for digit in guess_nobulls:
        if digit in number_nobulls:
            cows_index.append(digit)

    return cows_index


# function to check the game status and print the result

def give_result(b, c, x) -> bool:

    """
    b = bulls, c = cows, x = lives
    """

    global game_on

    bull_s = 'bulls'
    cow_s = 'cows'
    guess_es = 'guesses'

    if b == 1:
        bull_s = 'bull'
    if c == 1:
        cow_s = 'cow'
    if x == 1:
        guess_es = 'guess'

    if bulls != 4 and lives > 0:
        print(f'There are {b} {bull_s} and {c} {cow_s} in your number.\nYou have {x} {guess_es} left.')
        print(line)

        game_on = True

    elif bulls == 4:
        print(f'Congratulations, you win! And it only took you {20 - x} {guess_es}.\n' + 'One more game? ;-)')

        game_on = False

    elif bulls != 4 and lives == 0:
        print('Oh no, you just lost! 20 guesses were not enough...')

        game_on = False

    return game_on


# MAIN - GAME

print(head)
number_to_guess = '1234'

while game_on:

    guess = input()

    if guess.isnumeric() is False or len(guess) != 4 or guess[0] == '0':
        print('Invalid input, enter a 4-digit number.')

        continue

    lives -= 1
    bulls_index = check_bulls(number_to_guess, guess)
    number_nobulls = subtract_bulls(number_to_guess, bulls_index)
    guess_nobulls = subtract_bulls(guess, bulls_index)
    cows_index = check_cows(number_nobulls, guess_nobulls)
    bulls = len(bulls_index)
    cows = len(cows_index)
    give_result(b=bulls, c=cows, x=lives)

# game over :-)
