"""
Name: Brett Widholm
button.py

Problem: Acts as a class for the main function in lab10.py to use

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        label = self.text.getText()
        return label

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.text.draw(win)
        self.shape.draw(win)

    def undraw(self):
        self.text.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()

        if p1.getX() <= point.getX() <= p2.getX() and p1.getY() <= point.getY() <= p2.getY():
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)
