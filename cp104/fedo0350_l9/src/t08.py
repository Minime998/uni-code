'''
counts digits in string

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import digit_count

s = input("Enter a string: ")

count = digit_count(s)

print("There are {} digits".format(count))
