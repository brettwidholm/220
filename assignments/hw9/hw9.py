import random

def get_words(file_name):
    word_list = []
    file = open(file_name, 'r')
    file_lines = file.readlines()
    for i in file_lines:
        new_line = i.replace('\n', '')
        word_list.append(new_line)
    return word_list

def get_random_word(words):
    print(words[2])



def letter_in_secret_word(letter, secret_word):
    pass


def already_guessed(letter, guesses):
    pass


def make_hidden_secret(secret_word, guesses):
    pass


def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
