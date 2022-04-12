"""
Name: Brett Widholm
algorithims.py

Problem: Reads data_sorted.txt and manipulates that data to be used.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def read_data(filename):
    counter = 0
    file_list = []
    file = open(filename, 'r')
    file_xd = file.read()
    new_line_count = file_xd.count('\n')
    file.close()
    file_again = open(filename, 'r')
    file_text = file_again.readlines()
    while counter < (new_line_count + 1):
        acc = 0
        a = file_text[counter].split()
        while acc < len(a):
            file_list.append(eval(a[acc]))
            acc += 1
        counter += 1
    file.close()
    return file_list


def is_in_linear(search_val, values):
    counter = 0
    teleporter = 0
    while counter < len(values):
        if search_val == values[counter]:
            counter = len(values) + 1
            teleporter = (-1)
        counter += 1
    if teleporter < 0:
        return True
    else:
        return False
