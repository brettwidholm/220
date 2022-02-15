"""
Name: Brett Widholm
lab5.py

Problem: This program serves to solve a multitude of problems including (but not
limited to): creating a triangle and finding its area and perimeter, manipulating both
strings and lists, and summing a series. This program combines both graphical and console
elements in order to solve these problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

def triange():
    win = GraphWin("Make a triangle", 400, 400)

    point_1 = win.getMouse()
    point_2 = win.getMouse()
    point_3 = win.getMouse()

    triangle_shape = Polygon(point_1, point_2, point_3)
    triangle_shape.setFill('yellow')
    triangle_shape.draw(win)

    length_x1 = (point_2.getX()-point_1.getX())
    length_x2 = (point_3.getX() - point_2.getX())
    length_x3 = (point_1.getX() - point_3.getX())

    length_y1 = (point_2.getY()-point_1.getY())
    length_y2 = (point_3.getY() - point_2.getY())
    length_y3 = (point_1.getY() - point_3.getY())

    length_a = ((((length_x1)**2)+((length_y1)**2))**(1/2))
    length_b = ((((length_x2) ** 2) + ((length_y2) ** 2)) ** (1 / 2))
    length_c = ((((length_x3) ** 2) + ((length_y3) ** 2)) ** (1 / 2))

    s = ((length_a + length_b + length_c)/2)

    area = ((s*(s - length_a)*(s - length_b)*s - length_c)**(1/2))
    perimeter = (length_a + length_b + length_c)

    area_text = (Text(Point(200, 300), "Area:"))
    area_text.draw(win)
    area_value = (Text(Point(200, 325), area))
    area_value.draw(win)
    perimeter_text = (Text(Point(200, 350), "Perimeter:"))
    perimeter_text.draw(win)
    perimeter_value = (Text(Point(200, 375), perimeter))
    perimeter_value.draw(win)

    closing_text = (Text(Point(200, 25), "Click again to close"))
    closing_text.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    win.getMouse()
    red_entry_box = (Entry(Point(win_width / 2 + 50, win_height / 2 + 40), 15))
    red_entry_box.draw(win)
    win.getMouse()
    green_entry_box = (Entry(Point(win_width / 2 + 50, win_height / 2 + 70), 15))
    green_entry_box.draw(win)
    win.getMouse()
    blue_entry_box = (Entry(Point(win_width / 2 + 50, win_height / 2 + 100), 15))
    blue_entry_box.draw(win)
    win.getMouse()

    shape.setFill(color_rgb(eval(red_entry_box.getText()), eval(green_entry_box.getText()), eval(blue_entry_box.getText())))

    closing_text = (Text(Point(200, 25), "Click again to close"))
    closing_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input('Enter a string')

    concatenation = string[0] + string[-1]
    string_length = len(string)

    print(string[0])
    print(string[-1])
    print(string[1:5])
    print(concatenation)
    for i in range(10):
        print(string[0:3])
    for j in string:
        print(j)
    print(string_length)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    new_values = [values[2], values[3], values[0]]
    floats_and_integers = [values[2], values[0], float(values[-1])]


    x = (values[1] + values[3])
    print(x)
    x = (values[0]+values[2])
    print(x)
    x = (values[1]*5)
    print(x)
    x = values[2:5]
    print(x)
    x = new_values
    print(x)
    x = floats_and_integers
    print(x)
    x = (values[2] + values[0] + float(values[-1]))
    print(x)
    x = len(values)
    print(x)


def another_series():
    summation = 0
    term_number = eval(input('How many terms do you want to use? '))
    for i in range(term_number):
        summation = summation + (2*(1+(i % 3)))

    print('Sum =', summation)


def target():
    win = GraphWin("Target", 400, 400)

    yellow_circle = Circle(Point(200, 200), 12.5)
    red_circle = Circle(Point(200, 200), 25)
    blue_circle = Circle(Point(200, 200), 50)
    black_circle = Circle(Point(200, 200), 100)
    white_circle = Circle(Point(200, 200), 200)

    white_circle.draw(win)
    black_circle.draw(win)
    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_circle.draw(win)

    yellow_circle.setFill('yellow')
    red_circle.setFill('red')
    blue_circle.setFill('blue')
    black_circle.setFill('black')
    white_circle.setFill('white')

    closing_text = (Text(Point(200, 15), "Click to close"))
    closing_text.draw(win)

    win.getMouse()
    win.close()

