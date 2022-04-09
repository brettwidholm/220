"""
Name: Brett Widholm
hw10.py

Problem: This program use no for loops, solving sequences and manipulating lists
using while loops. As well, this program uses classes in order to manipulate
graphic objects.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import GraphWin, Point
from face import Face

def fibonacci(num):
    fibonacci_list = []
    count = 0
    initial_value = 1
    previous_value = 1
    while count != num:
        fibonacci_list.append(initial_value)
        term = initial_value + previous_value
        initial_value = previous_value
        previous_value = term
        count += 1
    return fibonacci_list[num-1]

def double_investment(principle, rate):
    years = 0
    interest = principle
    while interest <= (2 * principle):
        interest *= (1 + rate)
        years += 1
    return years

def syracuse(num):
    syracuse_list = []
    syracuse_list.append(num)

    while num != 1:
        if num % 2 == 0:
            num = (num // 2)
            syracuse_list.append(num)
        elif num % 2 != 0:
            num = (3 * num) + 1
            syracuse_list.append(num)

    return syracuse_list

def goldbach(num):
    primes = []
    chosen_primes = []
    acc = 1
    count = 0
    i = 0

    if num > 3:
        primes.append(2)
        primes.append(3)
    while acc <= (num//6):
        if acc <= 40:
            prime_number = (6 * acc) - 1
            prime_number_2 = (6 * acc) + 1
            primes.append(prime_number)
            primes.append(prime_number_2)
            acc += 1
        else:
            prime_number_3 = (acc ** 2) + acc + 41
            primes.append(prime_number_3)
            acc += 1

    if num % 2 != 0:
        return None
    elif num % 2 == 0:
        while count < (len(primes)):
            if (num - primes[count]) != primes[i]:
                i += 1
                if i >= (len(primes)):
                    i = 0
                    count += 1
            elif (num - primes[count]) == primes[i]:
                chosen_primes.append((num - primes[count]))
                chosen_primes.append(num - primes[i])
                count = 1 + (len(primes))
        chosen_primes.sort()
        return chosen_primes

def face_smile():
    win = GraphWin('Smile', 700, 700)
    face = Face(win, (Point(350, 350)), 150)
    face.smile()
    win.getMouse()
    win.close()

def face_shock():
    win = GraphWin('Smile', 700, 700)
    face = Face(win, (Point(350, 350)), 150)
    face.shock()
    win.getMouse()
    win.close()

def face_wink():
    win = GraphWin('Smile', 700, 700)
    face = Face(win, (Point(350, 350)), 150)
    face.wink()
    win.getMouse()
    win.close()
