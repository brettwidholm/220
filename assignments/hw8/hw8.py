"""
Name: Brett Widholm
hw8.py

Problem: This program modifies various lists in oder to produce new and
manipulated outputs.

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: Calvin Widholm
"""

import math
from graphics import GraphWin, Point, Text, Circle

def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    summation = 0
    for i in nums:
        summation = i + summation

    return summation


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])



def sum_of_squares(nums):
    output_list = []
    split_nums_list = []
    for i in range(len(nums)):
        split_nums = nums[i].split(',')
        split_nums_list.append(split_nums)
    for j in split_nums_list:
        to_numbers(j)
        square_each(j)
        cow = sum_list(j)
        output_list.append(cow)
    return output_list

def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199:
        return True
    if wins > 20:
        return True
    return False


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True

    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 +
        (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("pink")
    circle_two.draw(win)

    win.getMouse()

    if did_overlap(circle_one, circle_two):
        closing_text = (Text(Point(5, 5), "The circles overlap"))
        closing_text.draw(win)
    else:
        closing_text2 = (Text(Point(5, 5), "The circles do not overlap"))
        closing_text2.draw(win)

def did_overlap(circle_one, circle_two):
    center1 = circle_one.getCenter()
    center2 = circle_two.getCenter()
    radius1 = circle_one.getRadius()
    radius2 = circle_two.getRadius()

    distance = ((((center2.getX()-center1.getX())**2)+((center2.getY()-center1.getY())**2))**(1/2))
    radius_sum = radius1 + radius2

    if radius_sum >= distance:
        return True

    return False


if __name__ == '__main__':
    pass
