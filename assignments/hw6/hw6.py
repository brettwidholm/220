"""
Name: Brett Widholm
py6.py

Problem: This program servers to manipulate strings and lists in
order to get a desired outcome.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def cash_converter():
    int_value = eval(input('Enter an integer: '))
    print("That is ${:.2f}".format(int_value))


def encode():
    final_message = ''
    original_message = input("Enter a message")
    key = eval(input('Enter a key'))
    for i in original_message:
        encryption = ord(i) + key
        final_message = final_message + (chr(encryption))

    print(final_message)

def sphere_area(radius: float):
    area = (radius**2) * 4 * math.pi
    return area


def sphere_volume(radius: float):
    volume = (radius ** 3) * math.pi * (4/3)
    return volume


def sum_n(number: int):
    summation = 0
    for i in range(number):
        summation = (i+1) + summation

    return summation


def sum_n_cubes(number: int):
    summation = 0
    for i in range(number):
        summation = ((i+1)**3) + summation

    return summation


def encode_better():
    message_list = []
    key_list = []
    final_message = ''
    message = input('Enter a message: ')
    key = input('Enter a key: ')

    for i in message:
        message_list.append(ord(i)-65)

    for j in key:
        key_list.append(ord(j)-65)

    for k in range(len(message)):
        encryption = (message_list[k] + key_list[k % (len(key))]) % 58
        new_message = chr(encryption + 65)
        final_message = final_message + new_message

    print(final_message)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
