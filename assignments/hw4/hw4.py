"""
Name: Brett Widholm
hw4.py

Problem: This program serves to solve a wide variety of geometric and other
mathematical problems, giving the user visual examples to go along with the
calculations. The program can serve as an alternative to computing by hand.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import Circle, GraphWin, Rectangle, Point, Text


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw squares")
    instructions.draw(win)


    # builds a circle
    shape = Rectangle(Point(50, 50), Point(0, 0))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    shape_3 = shape.clone()
    shape_3.draw(win)


    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape_2 = shape.clone()
        shape_2.move(change_x, change_y)
        shape_2.draw(win)
        shape.move(change_x, change_y)
        i = i*0

    closing_text = (Text(Point(200, 200), "Click again to close"))
    closing_text.draw(win)




    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Build a Rectangle", 400, 400)
    Text(Point(200, 20), "Click two points to draw a rectangle")

    point_1 = win.getMouse()
    point_2 = win.getMouse()

    rectangle_shape = Rectangle(point_1, point_2)
    rectangle_shape.setFill('yellow')
    rectangle_shape.draw(win)

    length = (((point_2.getY()-point_1.getY())**2)**(1/2))
    width = (((point_2.getX()-point_1.getX())**2)**(1/2))
    area = (length * width)
    perimeter = (length + width) * 2

    area_text = (Text(Point(200, 300), "Area:"))
    area_text.draw(win)
    area_value = (Text(Point(200, 325), area))
    area_value.draw(win)
    perimeter_text = (Text(Point(200, 350), "Perimeter:"))
    perimeter_text.draw(win)
    perimeter_value = (Text(Point(200, 375), perimeter))
    perimeter_value.draw(win)

    closing_text = (Text(Point(200, 200), "Click again to close"))
    closing_text.draw(win)

    win.getMouse()
    win.close()

def circle():
    win = GraphWin("Build a Circle", 400, 400)
    Text(Point(200, 20), "Click two points to draw a circle")

    point_1 = win.getMouse()
    point_2 = win.getMouse()

    radius = (((point_2.getX() - point_1.getX())**2) + (point_2.getY() - point_1.getY())**2)**(1/2)

    circle_shape = Circle((point_1), radius)
    circle_shape.setFill('pink')
    circle_shape.draw(win)

    radius_text = (Text(Point(200, 350), "Radius:"))
    radius_text.draw(win)

    radius_value = (Text(Point(200, 375), radius))
    radius_value.draw(win)

    closing_text = (Text(Point(200, 200), "Click again to close"))
    closing_text.draw(win)
    win.getMouse()
    win.close()


def pi2():
    top_value = 0
    bottom_value = 0
    previous_value = 0
    user_input = eval(input('Enter the number of terms to sum: '))
    for i in range(1, user_input+1):
        bottom_value = bottom_value * 0
        bottom_value = bottom_value + ((2*i)-1)
        top_value = (4*((-1)**(i+1)))
        total = top_value/bottom_value
        previous_value = total + previous_value
        total = total*0

        top_value = (-1)

    print("Pi approximation:", previous_value)
    print('Accuracy:', abs(math.pi - previous_value))

if __name__ == '__main__':
    pass
