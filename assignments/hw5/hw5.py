"""
Name: Brett Widholm
hw5.py

Problem: This program manipulates with strings and lists in order to perform
certain tasks such as reversing the order of a name, shortening a name into its
initials, and converting text into pig latin.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = (input('Enter a name (first and last):'))
    split = name.split()
    comma = (split[-1] + ",")
    print(comma, split[0])

def company_name():
    company = (input('Enter a domain: '))
    split = company.split('.')
    print(split[1])

def initials():
    class_size = eval(input('How many students are in the class? '))
    for i in range(class_size):
        print('What is the name of student', i+1, '?')
        name = input('')
        split_name = name.split()
        first_initial = split_name[0]
        second_initial = split_name[1]
        print(first_initial[0] + second_initial[0])

def names():
    name_list = input('Enter a list of names: ')
    initial_list = []
    comma_remover = name_list.replace(',', '')
    split_names = comma_remover.split()
    for i in split_names:
        initial_list.append(i[0])

    term_number = len(initial_list)
    for j in range(0,term_number, 2):
        new_j_value = j+1
        print(initial_list[j] + initial_list[new_j_value], end=' ')


def thirds():
    sentence_number = eval(input('Enter the number of sentences'))
    sentence_list = []
    for i in range(sentence_number):
        print('Enter sentence', i+1)
        sentence = input('')
        new_sentence = (sentence[0::3])
        sentence_list.append(new_sentence)
    for j in range(sentence_number):
        print(sentence_list[j])


def word_average():
    sentence = input('Enter a sentence: ')
    split = sentence.split()
    sentence_no_space = (sentence.replace(' ', ''))
    characters = len(sentence_no_space)
    word_number = len(split)
    print('Average word length:', characters/word_number)

def pig_latin():
    sentence = input('Enter a sentence to be converted into pig latin: ')
    words = sentence.split()
    for i in words:
        i = i[1:] + i[0]
        i = i + 'ay'
        print(i.lower(), end=' ')


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
