"""
Name: Brett Widholm
lab12.py

Problem: This program imports data from files and allows the user to play a
higher-lower game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import random

def find_and_remove_first(list, value):
    count = 0
    while count < len(list):
        if value == list[count]:
            list.pop(count)
            list.insert(count, 'Brett')
            count = len(list) + 1738
        else:
            pass
        count += 1
    print(list)


def good_input():
    guess = 0
    while guess < 1 or guess > 10:
        guess = eval(input('Enter a number: '))
        if guess < 1:
            print('That guess is too low. ')
        elif guess > 10:
            print('That guess is too high.')
        else:
            return guess

def num_digits():
    num = 1
    output = 1738
    while num > 0:
        acc = 0
        num = eval(input('Enter a number: '))
        new_value = num
        while output != 0:
            output = new_value // 10
            new_value = output
            acc += 1
            if new_value == 0:
                print('This number had', acc, 'digits.')

def hi_lo_game():
    guesses = 7
    selected_value = random.randint(1, 100)
    while guesses != 0:
        user_guess = eval(input('Guess a number from 1 to 100: '))
        if user_guess < selected_value:
            print(user_guess, 'is too low of a guess.')
            guesses -= 1
            if guesses == 0:
                print('Sorry, you lose!')
                print('The numer was', selected_value)
        elif user_guess > selected_value:
            print(user_guess, 'is too high of a guess.')
            guesses -= 1
            if guesses == 0:
                print('Sorry, you lose!')
                print('The numer was', selected_value)
        elif user_guess == selected_value:
            print('Correct!!')
            print('You have won in', (7 - guesses), 'guesses!')
