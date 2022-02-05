"""
Name: Brett Widholm
hw3.py

Problem: This program serves to perform and calculate a wide variety of
mathematical equations in order to solve a variety of problems. The problems include,
but are no limited to: calculating an average grade, approximating a square root, and
calculating the value of pi.

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Calvin Widholm
"""


def average():
    number_of_grades = eval(input('How many grades will you enter? '))
    summation = 0
    for i in range(1, number_of_grades + 1):
        base_number = eval(input('Enter grade: '))
        summation = base_number + summation

    print('Your average is:', (summation/i))

def tip_jar():
    summation = 0
    for i in range(1, 6):
        donation_amount = eval(input('How much would you like to donate? '))
        summation = donation_amount + summation
        i = i*0

    print('Total tips:', summation)

def newton():
    root_number = eval(input('What number do you want to square root? '))
    approx_number = root_number
    approximation = eval(input('How many times should we improve the approximation? '))
    for i in range(1, approximation +1):
        approx_number = (approx_number + (root_number/approx_number))/2
        i = i*0

    print('The square root is approximately:', approx_number)


def sequence():
    term_number = eval(input('How many terms would you like? '))
    ini = 1
    for i in range(1, term_number + 1, 1):
        print(ini, end=' ')
        calculation = (1 + ((-1) ** i))
        ini = ini + calculation

def pi():
    term_number = eval(input('How many terms would you like in the series? '))
    ini_bottom = 1
    ini_top = 1
    previous_value = 1

    for i in range(1, term_number + 1, 1):
        bottom = (1 + ((-1) ** i)) / 2
        top = ((-1)**(i+1))/2
        ini_bottom = ini_bottom + (2 * bottom)
        ini_top = (((1+(2*i))+(2*top))/2)
        total = (ini_top / ini_bottom)
        total = previous_value * total
        previous_value = total

    print(2*previous_value)

if __name__ == '__main__':
    pass
