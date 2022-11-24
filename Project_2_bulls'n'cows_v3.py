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
----------------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
----------------------------------------------------
Enter your number (4 digits), but be careful, 
you only have 20 guesses!
----------------------------------------------------
'''

line = '-' * 52
game_on = True
players_choice = ''
lives = 20


# function to create a random 4-digit number

def give_number(length: int) -> str:
    """
    Returns a string with unique digits. Length of the string
    is the function´s parameter. 0 excluded on the first position.
    """

    number_range = range(1,length)
    pick_numbers = True
    number = str(random.randrange(1, 10))

    while pick_numbers:
        for digit in number_range:
            digit = str(random.randrange(10))
        if digit not in number:
            number += digit
        if len(number) == 4:
            pick_numbers = False

    return number


# function to identify "bulls" in the user's guess

def check_bulls(number_to_guess: str, guess: str) -> list:
    """
    Identifies positions with identical symbol within two strings
    of the same length ("number_to_guess", "guess") and returns
    a list with their indexes (in reversed order).
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
    Identifies values shared between two lists (not index dependent)
    and returns a list with their indexes.
    """

    cows_index = []

    for digit in guess_nobulls:
        if digit in number_nobulls and digit not in cows_index:
            cows_index.append(digit)

    return cows_index


# bulls and cows

def bulls_and_cows(bulls_index: list, cows_index: list) -> list:
    """
    Returns list with lengths of two lists given as parameters.
    """

    cattle = [len(bulls_index), len(cows_index)]

    return cattle


# function to evaluate the game status and inform the player

def give_result(cattle, lives, game_on) -> bool:
    """
    Evaluates the game status using parameters "cattle" and "lives" with three
    possible outcomes continue/win/lose. Prints the result and ends the game
    in case of win or loss.
    """

    bulls = cattle[0]
    cows = cattle[1]

    bull_s = 'bulls'
    cow_s = 'cows'
    guess_es = 'guesses'

    if bulls == 1:
        bull_s = 'bull'
    if cows == 1:
        cow_s = 'cow'
    if lives == 1:
        guess_es = 'guess'

    if bulls != 4 and lives > 0:
        print(f'There are {bulls} {bull_s} and {cows} {cow_s} in your number.\nYou have {lives} {guess_es} left.')
        print(line)

        game_on = True

    elif bulls == 4:
        print(f'Congratulations, you win! And it only took you {20 - lives} {guess_es}.\n' + 'One more game? ;-)')

        game_on = False

    elif bulls != 4 and lives == 0:
        print('Oh no, you just lost! 20 guesses were not enough...')

        game_on = False

    return game_on


# main - set off the game

def main(game_on, lives):

    number_to_guess = give_number(4)

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
        cattle = bulls_and_cows(bulls_index, cows_index)
        game_on = give_result(cattle, lives, game_on)

# main

if __name__ == "__main__":

    print(head)
    main(game_on, lives)




