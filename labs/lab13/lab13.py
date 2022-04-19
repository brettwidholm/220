"""
Name: Brett Widholm
lab13.py

Problem: The program is designed to assist the user with trading, giving them alerts
for when certain events occur.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    file = open(filename, 'r')
    file_text = file.read()
    split_text = file_text.split()
    for i in range(len(split_text)):
        if eval(split_text[i]) > 830:
            print('Warning, the trades have exceeded 830 trades per seconds!!')
            print('This message was triggered at', (i+1), 'seconds.')
        elif eval(split_text[i]) == 500:
            print('Pay attention!! There are exactly 500 trades in one second.')
            print('This message was triggered at', (i+1), 'seconds.')
        else:
            pass
    file.close()
