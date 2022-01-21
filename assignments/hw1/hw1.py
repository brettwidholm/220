"""
Name: Brett Widholm
hw1.py

Problem: <This program uses various mathematical equations to calculate solutions to
a multitude of problems quickly. This program offers shortcuts for users, sparing them
of their own calculations and completing the job for them.>

Certification of Authenticity:

I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input('Enter the length: '))
    width = eval(input('Enter the width: '))
    area = length*width
    print('Area =', area)

def calc_volume():
    length = eval(input('Enter the length: '))
    width = eval(input('Enter the width: '))
    height = eval(input('Enter the height: '))
    volume = length*width*height
    print('Volume =', volume)

def shooting_percentage():
    shots = eval(input("Enter the player's total shots: "))
    shotsmade = eval(input(' Enter how many shots the player made: '))
    shootingpercent = shotsmade/shots*100
    print('Shooting percentage:', shootingpercent, '%')

def coffee():
    pounds_of_coffee = eval(input('How many pounds of coffee would you like? '))
    total = (10.50*pounds_of_coffee)+(0.86*pounds_of_coffee)+1.50
    print('Your total is:', total)

def kilometers_to_miles():
    kilometers = eval(input('How many kilometers did you travel? '))
    miles = kilometers/1.61
    print("That's", miles, 'miles!')

if __name__ == '__main__':
    pass
