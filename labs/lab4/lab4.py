"""
Name: Brett Widholm
lab4.py

Problem: This program uses the Python Graphics Library in order to make
an animated Valentine's Day card. The program tells the recipient "Happy Valentine's
Day" and shoots an animated arrow through a heart.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import time
from graphics import *

def greeting_card():

    window = GraphWin("Valentine's Card", 700, 700)

    text = Text(Point(350, 50), "Happy Valentine's Day!!")
    text.draw(window)

    arrow_bottom = Polygon(Point(0, 325), Point(0, 375), Point(25, 350))
    arrow_bottom.draw(window)
    arrow_body = Rectangle(Point(10, 355), Point(75, 345))
    arrow_body.draw(window)
    arrow_head = Polygon(Point(75, 325), Point(75, 375), Point(100, 350))
    arrow_head.draw(window)
    arrow_bottom.setFill('brown')
    arrow_bottom.setOutline('brown')
    arrow_body.setFill('brown')
    arrow_body.setOutline('brown')
    arrow_head.setFill('gray')
    arrow_head.setOutline('gray')

    heart_bottom = Polygon(Point(350, 500), Point(500, 300), Point(200, 300))
    heart_top_left = Circle(Point(425, 250), 90)
    heart_top_right = Circle(Point(275, 250), 90)

    heart_bottom.setFill('pink')
    heart_top_right.setFill('pink')
    heart_top_left.setFill('pink')

    heart_bottom.setOutline('pink')
    heart_top_right.setOutline('pink')
    heart_top_left.setOutline('pink')

    heart_bottom.draw(window)
    heart_top_left.draw(window)
    heart_top_right.draw(window)


    for i in range(100):
        time.sleep(0.1)
        arrow_body.move(7, 0)
        arrow_head.move(7, 0)
        arrow_bottom.move(7, 0)

    closer = Text(Point(350, 600), "Click anywhere to close")
    closer.draw(window)

    window.getMouse()
    window.close()
