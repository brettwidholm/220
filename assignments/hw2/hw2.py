"""
Name: Brett Widholm
hw2.py

Problem: This program seeks to assist users with mathematics, solving problems
dealing with area and summation. As well, the program also performs more basic functions
such as solving a base number raised to a certain power and printing out a multiplication
table (10x10).

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Calvin Widholm>
"""
import math


def sum_of_threes():
    upper_bound = eval(input('What is the upper bound? '))
    trunkate = (upper_bound//3)
    summation = 0
    for i in range(1, trunkate+1):
        summation = summation+(i*3)

    print('Sums of threes is', summation)


def multiplication_table():
    for i in range(1, 11):
        print(end='\n')
        for j in range(1, 11):
            table = j*i
            print(table, end="\t")


def triangle_area():
    side_a = eval(input('Enter side A length: '))
    side_b = eval(input('Enter side B length: '))
    side_c = eval(input('Enter side C length: '))
    s_value = (side_a + side_b + side_c)/2
    area_of_triangle = math.sqrt(s_value*((s_value - side_a)*(s_value - side_b)*(s_value - side_c)))
    print('The area is', area_of_triangle)

def sum_squares():
    lower_range = eval(input('Enter the lower range: '))
    upper_range = eval(input('Enter the upper range: '))
    sum_of_squares = 0
    for i in range(lower_range, upper_range+1):
        sum_of_squares = sum_of_squares+(i**2)

    print('Sum of squares is', sum_of_squares)


def power():
    base_number = eval(input('Enter base: '))
    exponent_number = eval(input("Enter exponent: "))
    power_value = base_number
    for i in range(exponent_number-1):
        power_value = power_value * base_number
        i = i*0

    print(power_value)

if __name__ == '__main__':
    pass
