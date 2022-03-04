"""
Name: Brett Widholm
hw7.py

Problem: This program manipulates files to transfer data into various different
files.

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Calvin Widholm
"""

from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    counter = 0
    file = open(in_file_name, 'r')
    file_text = file.read()
    replacement = file_text.replace('\n', ' ')
    split = replacement.split()
    file.close()
    file2 = open(out_file_name, 'w')
    for i in split:
        counter = counter + 1
        print(counter, i, file=file2)

    file2.close()


def hourly_wages(in_file_name, out_file_name):
    file = open(in_file_name, 'r')
    file_text = file.readlines()
    file2 = open(out_file_name, 'w')
    for i in file_text:
        split = i.split(' ')
        first_name = split[0]
        last_name = split[1]
        pay = float(split[2]) + 1.65
        hours = float(split[3])
        weeks_pay = hours * pay
        print(first_name, last_name, "{:.2f}".format(weeks_pay), file=file2)
    file.close()
    file2.close()

def calc_check_sum(isbn):
    numbers = []
    total = 0
    no_hyphens = isbn.replace('-', '')
    for i in no_hyphens:
        numbers.append(i)
    list_length = len(numbers)
    for j in range(list_length):
        total = total + (int(numbers[j]) * list_length)
        list_length = list_length - 1
    return total

def send_message(file_name, friend_name):
    file = open(file_name, 'r')
    file_text = file.read()
    file2 = (friend_name + '.txt')
    file2_text = open(file2, 'w')
    print(file_text.rstrip(), file=file2_text)


def send_safe_message(file_name, friend_name, key):
    file = open(file_name, 'r')
    file_text = file.read()
    encoded_text = encode(file_text, key)
    new_lines = chr((ord('\n') + key))
    new_encoded_text = encoded_text.replace(new_lines, '\n')
    file2 = (friend_name + '.txt')
    file2_text = open(file2, 'w')
    print(new_encoded_text.rstrip(), file=file2_text)

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name, 'r')
    file_text = file.read()
    pad_file = open(pad_file_name, 'r')
    pad_file_key = pad_file.read()
    encoded_text = encode_better(file_text, pad_file_key)
    file2 = friend_name + '.txt'
    file2_text = open(file2, 'w')
    print(encoded_text, file=file2_text)

if __name__ == '__main__':
    pass
