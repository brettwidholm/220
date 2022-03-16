"""
Name: Brett Widholm
lab8.py

Problem: This program used two files in order to read and intake information
and output manipulated data.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    names = []
    grades = []
    all_values = []
    length = []
    averages = []
    counter = 0
    value_counter = 0
    class_sum = 0
    file = open(in_file_name, 'r')
    file_2 = open(out_file_name, 'w')
    for i in file:
        strip = i.strip()
        split = strip.split(':')
        names.append(split[0])
        grades.append(split[1])
    for j in range(len(grades)):
        counter = counter * 0
        isolated_grades = (grades[j].strip())
        newest_grades = (isolated_grades.split())
        for k in newest_grades:
            full_number = eval(k[0]+k[1])
            all_values.append(full_number)
        length.append(len(newest_grades))

    for l in length:
        final_average = 0
        weight_counter = 0
        for m in range(0, int(l), 2):
            average = (all_values[value_counter])*(all_values[value_counter+1])
            final_average = average + final_average
            weight_average = (all_values[value_counter])
            weight_counter = weight_average + weight_counter
            value_counter = value_counter + 2
        student_average = (final_average/100)

        if weight_counter == 100:
            print(names[counter] + "'s average:", student_average, file=file_2)
            averages.append(student_average)
            counter = counter + 1
        elif weight_counter < 100:
            print(names[counter] + "'s average: Error: The weights are less than 100.", file=file_2)
            counter = counter + 1
        elif weight_counter > 100:
            print(names[counter] + "'s average: Error: The weights are more than 100.", file=file_2)
            counter = counter + 1
    for z in range(len(averages)):
        class_sum = averages[z] + class_sum
    print('Class average:', (class_sum/(len(averages))), file=file_2)

    file.close()
    file_2.close()
