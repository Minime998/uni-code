'''
test the severity of an earthquake

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-22"

'''
from functions import richter

intensity = float(input("Richter Scale Number: "))

result = richter(intensity)

print(result)