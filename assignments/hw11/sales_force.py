"""
Name: Brett Widholm
sales_force.py

Problem: This creates a sales force class that keeps track of the employees
and can compare their accomplishments and individal achievement.

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: Calvin Widholm
"""

from sales_person import SalesPerson

class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        file_text = file.readlines()

        for i in file_text:
            split_line = i.split(',')
            employ_id = eval(split_line[0])
            employ_name = split_line[1].strip()
            employee = SalesPerson(employ_id, employ_name)

            employ_sales = split_line[2].strip()
            sale_amounts = employ_sales.split()
            for j in range(len(sale_amounts)):
                employee.enter_sale(eval(sale_amounts[j]))
            self.sales_people.append(employee)

    def quota_report(self, quota):
        outter_list = []

        for i in self.sales_people:
            inner_list = []
            inner_list.append(i.get_id())
            inner_list.append(i.get_name())
            inner_list.append(i.total_sales())
            inner_list.append(i.met_quota(quota))
            outter_list.append(inner_list)

        return outter_list

    def top_seller(self):
        top_sellers = []
        for i in self.sales_people:
            employ_sale = i.get_sales()
            employ_sale.sort()
            for j in range(len(employ_sale)):
                if employ_sale[-1] == employ_sale[j]:
                    top_sellers.append(employ_sale[-1])
                    top_sellers.append(employ_sale[j])
                elif employ_sale[-1] != employ_sale[j]:
                    top_sellers.append(employ_sale[-1])
        return top_sellers

    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if employee_id == i.get_id():
                return i

    def get_sale_frequencies(self):
        dictionary = {}
        for i in self.sales_people:
            employ_sales = i.get_sales()
            for j in employ_sales:
                if j in dictionary:
                    dictionary[j] += 1
                else:
                    dictionary[j] = 1

        return dictionary
