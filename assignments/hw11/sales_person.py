"""
Name: Brett Widholm
sales_person.py

Problem: This creates a sales person class consisting of the components that
make up the sales person and consisting functions that can help compare
different sales people.

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: Calvin Widholm
"""

class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        for i in range(len(self.sales)):
            acc += self.sales[i]
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        if self.total_sales() < other.total_sales():
            return -1
        if self.total_sales() == other.total_sales():
            return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())
