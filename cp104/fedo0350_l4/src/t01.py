'''
Diameter of circle

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-08"

'''
from functions import diameter

diam_of_circle = float(input("Enter radius: "))

diam = diameter(diam_of_circle)

print("Diameter of circle: {:.2f}".format(diam))
