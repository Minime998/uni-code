'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import factorial

num = int(input("Enter a positive number: "))

if num >= 0:
    fact = factorial(num)
    print("{}! = {}".format(num, fact))
else:
    print("Error: you entered a negative number")
