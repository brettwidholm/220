"""
Name: Brett Widholm
lab6.py

Problem: Manipulates strings in order to encrypt a user-chosen message

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

def Vigenere():
    key_terms = []
    initial_message = ''

    win = GraphWin('Vigenere', 600, 400)

    entry_box = Entry(Point(350, 50), 25)
    entry_box.draw(win)
    entry_box_2 = Entry(Point(350, 100), 25)
    entry_box_2.draw(win)
    encode_box = Rectangle(Point(250, 225), Point(350, 175))
    encode_box.draw(win)

    box_text = (Text(Point(300, 200), "Encode"))
    box_text.draw(win)
    message_text = (Text(Point(75, 50), "Message to Code"))
    message_text.draw(win)
    key_text = (Text(Point(75, 100), "Enter Keyword"))
    key_text.draw(win)

    win.getMouse()

    message_text = entry_box.getText()
    capital_message = message_text.upper()
    message = capital_message.replace(' ', '')

    key_text = entry_box_2.getText()
    capital_key = key_text.upper()
    key = capital_key.replace(' ', '')
    key_length = len(key)

    encode_box.undraw()
    box_text.undraw()

    for j in key:
        key_terms.append(ord(j))

    for i in range(len(message)):
        message_ord = ord(message[i]) - 65
        final_key = i % (key_length)
        message_key_sum = message_ord + (key_terms[final_key] - 65)
        message_character = ((message_key_sum) % 26)
        final_message = (chr(message_character+65))
        initial_message = initial_message + final_message

    resulting_message = (Text(Point(300, 300), "Resulting Message"))
    resulting_message.draw(win)
    actual_message = (Text(Point(300, 325), initial_message))
    actual_message.draw(win)
    closing_text = (Text(Point(300, 375), "Click to close"))
    closing_text.draw(win)

    win.getMouse()
    win.close()