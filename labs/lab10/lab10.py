"""
Name: Brett Widholm
lab10.py

Problem: Imports and uses the classes 'Button' and 'Door' to make a door that opens
and closes

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
from button import Button
from door import Door

def main():
    win = GraphWin('Button', 600, 700)
    button_rectangle = Rectangle(Point(150, 50), Point(450, 200))
    door_rectangle = Rectangle(Point(150, 300), Point(450, 700))
    button = Button(button_rectangle, 'Exit')
    door = Door(door_rectangle, 'Closed')

    clicker = win.getMouse()
    while button.is_clicked(clicker) == False:

        if door.is_clicked(clicker) == True and door.get_label() == 'Open':
            door.closed('red', 'Closed')
        elif door.is_clicked(clicker) == True and door.get_label() == 'Closed':
            door.open('white', 'Open')
        clicker = win.getMouse()

    win.close()

