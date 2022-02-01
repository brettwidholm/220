"""
Name: Brett Widholm
lab3.py

Problem: This program serves to analyze traffic patterns, giving the user the average number of
cars on a road per day, the total number of vehicles on all roads surveyed, and the average
number of vehicles per road. The program asks for user inputs, performing all calculations and
giving the results of those calculations back to the user.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def traffic():

    road_number = eval(input('How many roads were surveyed? '))
    total_vehicles = 0
    total_days = 0
    car_average = 0

    for i in range(1, road_number +1):
        car_average = car_average*0
        print('How many days was road', i, 'surveyed for?')
        number_of_days = eval(input(""))
        total_days = number_of_days + total_days
        for j in range(1, number_of_days +1):
            print('How many cars traveled on day', j, '?')
            number_of_cars = eval(input(''))
            car_average = car_average + number_of_cars
            total_vehicles = total_vehicles + number_of_cars

        print('Road', i, 'average:', (round((car_average/number_of_days), 2)))

    print('Total number of vehicles on all roads:', total_vehicles)
    print('Average number of vehicles per road:', (round((total_vehicles/road_number), 2)))