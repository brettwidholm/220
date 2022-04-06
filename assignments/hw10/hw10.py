def fibonacci(n):
    count = 0
    initial_value = 1
    previous_value = 0
    while count != n:

        initial_value += previous_value
        previous_value = initial_value
        count += 1
        print(initial_value)
