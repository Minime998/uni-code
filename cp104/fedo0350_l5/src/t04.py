'''
finds closest number to target

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-22"

'''
from functions import closest

target = float(input("Enter the target: "))
v1 = float(input("Enter v1: "))
v2 = float(input("Enter v2: "))

result = closest(target, v1, v2)

print("Closest value to {} is {}".format(target, result))
