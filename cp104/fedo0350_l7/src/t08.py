'''
gets the expenses of the budget along with what type
it is

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import budget

available = float(input("Monthly budget: "))

expenses, balance, status = budget(available)

print("""Total expenses: ${:.2f}
{}: ${:.2f}""".format(expenses,status,balance))