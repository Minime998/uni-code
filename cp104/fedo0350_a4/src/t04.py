'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-25"

'''
from functions import pocket_colour

col = int(input("Enter a pocket number: "))

result = pocket_colour(col)

print("The selected pocket is {}.".format(result))
