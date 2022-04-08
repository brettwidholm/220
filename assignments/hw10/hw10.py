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

def fibonacci(n):
    fibonacci_list = []
    count = 0
    initial_value = 1
    previous_value = 1
    while count != n:
        fibonacci_list.append(initial_value)
        term = initial_value + previous_value
        initial_value = previous_value
        previous_value = term
        count += 1
    return fibonacci_list[n-1]

def double_investment(principle, rate):
    years = 0
    interest = principle
    while interest <= (2 * principle):
        interest = principle * (1 + rate)
        years += 1
    return years

def syracuse(n):
    syracuse_list = []
    syracuse_list.append(n)

    while n != 1:
        if n % 2 == 0:
            n = (n // 2)
            syracuse_list.append(n)
        elif n % 2 != 0:
            n = (3 * n) + 1
            syracuse_list.append(n)

    return syracuse_list

def goldbach(n):
    primes = []
    chosen_primes = []
    acc = 1
    count = 0
    i = 0


    if n > 3:
        primes.append(2)
        primes.append(3)
    while acc <= (n / 6):
        prime_number = (6 * acc) - 1
        prime_number_2 = (6 * acc) + 1
        primes.append(prime_number)
        primes.append(prime_number_2)
        acc += 1

    if n % 2 != 0:
        return None
    elif n % 2 == 0:
        while count < (len(primes)):
            if (n - primes[count]) != primes[i]:
                i += 1
                if i >= (len(primes)):
                    i = 0
                    count += 1
            elif (n - primes[count]) == primes[i]:
                chosen_primes.append((n - primes[count]))
                chosen_primes.append(n - primes[i])
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
