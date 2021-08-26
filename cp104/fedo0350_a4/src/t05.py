'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-25"

'''
from functions import colour_mix

pri = input("Enter a first colour: ")

sec = input("Enter a second colour: ")

result = colour_mix(pri, sec)

print("The mixed colour is {}.".format(result))
