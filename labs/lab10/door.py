"""
Name: Brett Widholm
door.py

Problem: Acts as a class for the main function in lab10.py to use

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        label = self.text.getText()
        return label

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()

        if p1.getX() <= point.getX() <= p2.getX() and p1.getY() <= point.getY() <= p2.getY():
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def closed(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret == False:
            return False
        else:
            return True

    def set_secret(self, secret):
        self.secret = secret
