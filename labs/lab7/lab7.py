"""
Name: Brett Widholm
lab7.py

Problem: This program creates virtual bumper cars, simulating their collisions
and how they might act.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# I HAD SOME PROBLEM WITH EDGE BUGGING BUT WAS CLEARED.

from graphics import *
from random import *
import time

def get_random(movement: int):
    random_integer = randint(-movement, movement)
    return random_integer

def did_collide(circle, circle2):
    circle_point = circle.getCenter()
    circle2_point = circle2.getCenter()
    distance = ((((circle2_point.getX()-circle_point.getX())**2)+((circle2_point.getY()-circle_point.getY())**2))**(1/2))
    radius_sum = circle.getRadius() + circle2.getRadius()

    if radius_sum >= distance:
        return True
    else:
        return False

def hit_vertical(ball, win):
    ball_point = ball.getCenter()

    if ball_point.getY() >= win.getHeight()-ball.getRadius():
        return True
    elif ball_point.getY() <= ball.getRadius():
        return True
    else:
        return False
def hit_horizontal(ball, win):
    ball_point = ball.getCenter()

    if ball_point.getX() >= win.getWidth() - ball.getRadius():
        return True
    elif ball_point.getX() <= ball.getRadius():
        return True
    else:
        return False
def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)

    return color

def bumper():
    win = GraphWin("Bumper", 400, 400)

    circle = Circle(Point(randint(26, 374), randint(26, 374)), 25)
    circle2 = Circle(Point(randint(26, 374), randint(26, 374)), 25)

    circle.setFill(get_random_color())
    circle2.setFill(get_random_color())

    circle.draw(win)
    circle2.draw(win)

    win.checkMouse()

    rand_value_x = get_random(10)
    rand_value_y = get_random(10)
    rand_value_x2 = get_random(10)
    rand_value_y2 = get_random(10)

    while win.checkMouse() == None:
        time.sleep(0.1)

        circle.move(rand_value_x, rand_value_y)
        circle2.move(rand_value_x2, rand_value_y2)

        if did_collide(circle, circle2) == True:
            rand_value_x = rand_value_x * -1
            rand_value_y = rand_value_y * -1
            rand_value_x2 = rand_value_x2 * -1
            rand_value_y2 = rand_value_y2 * -1

        if hit_vertical(circle, win) == True:
            rand_value_x = rand_value_x * 1
            rand_value_y = rand_value_y * -1

        if hit_vertical(circle2, win) == True:
            rand_value_x2 = rand_value_x2 * 1
            rand_value_y2 = rand_value_y2 * -1

        if hit_horizontal(circle, win) == True:
            rand_value_x = rand_value_x * -1
            rand_value_y = rand_value_y * 1

        if hit_horizontal(circle2, win) == True:
            rand_value_x2 = rand_value_x2 * -1
            rand_value_y2 = rand_value_y2 * 1

    else:
        win.close()
