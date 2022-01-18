"""
Brett Widholm

lab1.py

The problem that this program solves is showing the monthly interest rates on credit card accounts by showing the user their average monthly interest charge.

I certify that this assignment is entirely my own work.

"""

#inputs
annualinterest = eval(input('What is your annual interest rate (percent value)? '))
billingcycle = eval(input("What is the number of days in your billing cycle? "))
previousbalance = eval(input("What was your previous balance? "))
paymentamount = eval(input('What is your payment amount? '))
paymentday = eval(input('On what day of the cycle did you make your payment? '))

#calculations
netbalance_by_billingcycle = previousbalance*billingcycle
paymentamount_by_day = paymentamount*(billingcycle-paymentday)
netbalance_minus_paymentamount = netbalance_by_billingcycle-paymentamount_by_day
average_dailybalance = netbalance_minus_paymentamount/billingcycle
monthlyinterest = average_dailybalance*(annualinterest/12/100)
rounded_monthlyinterest = round(monthlyinterest, 2)

print('Your monthly interest charge is: $', rounded_monthlyinterest)

