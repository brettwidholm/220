"""
Name: Brett Widholm
lab2.py

Problem: This program solves for three different types of means: root-mean-squares,
harmonic means, and geometric means. The program takes the user's inputted values,
plugging them into three separate mean equations and effortlessly calculates the three
types of means.

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Lab instructors
"""

number_of_values = eval(input('How many values do you want? '))

rms_stored_values = []
hm_stored_values = []
gm_stored_values = []

for i in range(number_of_values):
    user_input = eval(input('Enter you value: '))
    user_input_squared = (user_input**2)
    user_input_divided = (1/user_input)
    rms_stored_values.append(user_input_squared)
    hm_stored_values.append(user_input_divided)
    gm_stored_values.append(user_input)

gm_initial_value = 1
for x in gm_stored_values:
    gm_initial_value = x * gm_initial_value

rms_calculation = (((sum(rms_stored_values))/number_of_values)**(1/2))
hm_calculation = (number_of_values/(sum(hm_stored_values)))
gm_calculation = (gm_initial_value ** (1/number_of_values))
print('Your Root-Mean-Square is', round(rms_calculation, 3))
print('Your Harmonic Mean is', round(hm_calculation, 3))
print('Your Geometric Mean is', round(gm_calculation, 3))

