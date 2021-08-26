'''
gets a string value of a digit from a list

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import get_digit_name

strnum = int(input("Enter a number between 0-9: "))

name = get_digit_name(strnum)

print("This is your number: {}".format(name))
