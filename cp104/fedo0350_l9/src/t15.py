'''
treats a string as a math expression and evals it

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import calculate

expr = input("Enter an expression: ")

result = calculate(expr)

print("{} = {}".format(expr,result))