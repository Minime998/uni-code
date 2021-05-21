'''
gives a workers salary to retirement

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-29"

'''
from functions import retirement

age = int(input("Enter the worker's age: "))
salary = int(input("Enter the worker's salary: "))
increase = float(input("Enter the yearly raise (%): "))

retirement(age, salary, increase)

