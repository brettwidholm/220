"""
Name: Brett Widholm
hw9.py

Problem: This program allows the user to play the game "Hangman" in both graphical
and command prompt interfaces.

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: Calvin Widholm
"""


import random
from graphics import GraphWin, Point, Text, Line, Circle, Entry

def get_words(file_name):
    words = []
    file = open(file_name, 'r')
    file_lines = file.readlines()
    for i in file_lines:
        words.append(i)
    get_random_word(words)
    return words


def get_random_word(words):
    random_int = random.randint(0, len(words) - 1)
    secret_word = words[random_int]
    new_secret_word = secret_word.replace('\n', '')
    return new_secret_word



def letter_in_secret_word(letter, secret_word):
    letter_is_true = secret_word.find(letter)

    if letter_is_true == (-1):
        return False
    return True

def already_guessed(letter, guesses):
    letters_used = guesses
    for i in letters_used:
        if letter == i:
            return True
    return False

def make_hidden_secret(secret_word, guesses):
    guesser = []
    empty = ''
    for i in range(len(secret_word)):
        guesser.append('_ ')
        i = i * 0
    for j in range(len(guesses)):
        for k in range(len(secret_word)):
            if guesses[j] == secret_word[k]:
                guesser[k] = guesses[j] + ' '

    for letter in guesser:
        empty = empty + letter

    stripped = empty.rstrip()

    return stripped



def won(guessed):
    split = guessed.split()
    for i in split:
        if i == '_':
            return False
    return True


def play_graphics(secret_word):
    win = GraphWin('Hangman', 700, 700)
    indicator = (Text(Point(350, 25), 'Letters:'))
    letters = (Text(Point(350, 50), 'a  b  c  d  e  f  g  h  i  j  k  l  m  n  '
                                    'o  p  q  r  s  t  u  v  w  x  y  z'))
    instruction = (Text(Point(350, 675), 'Click to confirm letter'))
    letter_guess = (Text(Point(150, 650), 'Guess a letter'))
    already_guessed_text = (Text(Point(500, 250), 'Letters you have guessed:'))

    gallow_body = Line(Point(350, 200), Point(350, 500))
    gallow_bottom = Line(Point(250, 500), Point(450, 500))
    gallow_top = Line(Point(350, 200), Point(250, 200))
    rope = Line(Point(250, 200), Point(250, 250))

    head = Circle(Point(250, 275), 25)
    body = Line(Point(250, 300), Point(250, 400))
    left_arm = Line(Point(250, 325), Point(200, 375))
    right_arm = Line(Point(250, 325), Point(300, 375))
    left_leg = Line(Point(250, 400), Point(200, 475))
    right_leg = Line(Point(250, 400), Point(300, 475))

    already_guessed_text.draw(win)
    letters.draw(win)
    indicator.draw(win)
    letter_guess.draw(win)
    instruction.draw(win)

    gallow_body.draw(win)
    gallow_bottom.draw(win)
    gallow_top.draw(win)
    rope.draw(win)

    guesses_remaining = 6
    guess_list = []
    word = secret_word

    winner = (Text(Point(350, 100), 'Winner!'))
    revealed_word = (Text(Point(350, 600), word))

    while guesses_remaining > 0:
        if guesses_remaining == 5:
            head.undraw()
            head.draw(win)
        if guesses_remaining == 4:
            body.undraw()
            body.draw(win)
        if guesses_remaining == 3:
            left_arm.undraw()
            left_arm.draw(win)
        if guesses_remaining == 2:
            right_arm.undraw()
            right_arm.draw(win)
        if guesses_remaining == 1:
            left_leg.undraw()
            left_leg.draw(win)
        have_guessed = (Text(Point(500, 275), guess_list))
        have_guessed.draw(win)
        letter_guess = (Text(Point(350, 600), make_hidden_secret(word, guess_list)))
        letter_guess.draw(win)
        entry_box = Entry(Point(350, 650), 25)
        entry_box.draw(win)
        win.getMouse()
        user_guess = entry_box.getText()
        while already_guessed(user_guess, guess_list):
            win.getMouse()
            user_guess = entry_box.getText()
        while not already_guessed(user_guess, guess_list):
            guess_list.append(user_guess)
            letter_guess.undraw()
            have_guessed.undraw()
            if letter_in_secret_word(user_guess, word):
                pass
            elif not letter_in_secret_word(user_guess, word):
                guesses_remaining = guesses_remaining - 1
        if won(make_hidden_secret(word, guess_list)):
            letter_guess.undraw()
            entry_box.undraw()
            have_guessed.draw(win)
            winner.draw(win)
            revealed_word.draw(win)
            guesses_remaining = 0
            win.getMouse()
            win.close()
        elif not won(make_hidden_secret(word, guess_list)) and guesses_remaining == 0:
            right_leg.draw(win)
            failure = (Text(Point(350, 100), 'Sorry, you did not guess the word.'))
            losing_word = (Text(Point(350, 125), 'The word was:'))
            losing_reveal = (Text(Point(350, 150), word))
            letter_guess.undraw()
            entry_box.undraw()
            failure.draw(win)
            losing_word.draw(win)
            losing_reveal.draw(win)
            win.getMouse()
            win.close()


def play_command_line(secret_word):
    guesses_remaining = 6
    guess_list = []
    word = secret_word

    while guesses_remaining > 0:
        print('Guesses remaining:', guesses_remaining)
        print('Already guessed:', guess_list)
        print(make_hidden_secret(word, guess_list))
        user_guess = input('Guess a letter: ')
        while already_guessed(user_guess, guess_list):
            print("You've already guessed that letter, please try again")
            print(make_hidden_secret(word, guess_list))
            user_guess = input('Guess a letter: ')
        while not already_guessed(user_guess, guess_list):
            guess_list.append(user_guess)
            if letter_in_secret_word(user_guess, word):
                pass
            elif not letter_in_secret_word(user_guess, word):
                guesses_remaining = guesses_remaining - 1
        if won(make_hidden_secret(word, guess_list)):
            print('Winner!')
            print(word)
            guesses_remaining = 0
        elif not won(make_hidden_secret(word, guess_list)) and guesses_remaining == 0:
            print('Sorry, you did not guess the word.')
            print('The word was', word)



if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
