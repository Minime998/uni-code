'''
calculates new payment

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-22"

'''
from functions import get_pay

emp_id = int(input("Employee ID: "))
hourly_rate = float(input("Hourly wage rate: "))
hours_worked = float(input("Hours worked: "))

net_payment = get_pay(hourly_rate, hours_worked)

print("Net payment for employee {}: ${:.2f}".format(emp_id, net_payment))
