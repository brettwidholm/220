"""
Name: Brett Widholm
algorithims.py

Problem: This program serves to sort different lists for the user to improve
ogranization.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

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

def selection_sort(values):
    for i in range(len(values)):
        bot_value = i
        for j in range((bot_value + 1), len(values)):
            if values[j] < values[bot_value]:
                bot_value = j

        list_sort = values[i]
        values[i] = values[bot_value]
        values[bot_value] = list_sort

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    x_1, x_2 = p1.getX(), p2.getX()
    y_1, y_2 = p1.getY(), p2.getY()
    area = (abs(x_2 - x_1)) * (abs(y_2 - y_1))
    return area

def rect_sort(rectangles):
    area_list = []
    for i in rectangles:
        output = calc_area(i)
        area_list.append(output)
    for z in range(len(area_list)):
        bot_value = z
        for j in range((bot_value + 1), len(rectangles)):
            if area_list[j] < area_list[bot_value]:
                bot_value = j

        rectangle_sort = rectangles[z]
        rectangles[z] = rectangles[bot_value]
        rectangles[bot_value] = rectangle_sort

        area_sort = area_list[z]
        area_list[z] = area_list[bot_value]
        area_list[bot_value] = area_sort
