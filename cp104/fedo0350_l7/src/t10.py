'''
get multiple employee net payments and average

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-05"

'''
from functions import employee_payroll

total, average = employee_payroll()

print("""Total payment: ${:,.2f}
Average payment: ${:,.2f}""".format(total,average))
