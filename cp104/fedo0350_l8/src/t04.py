'''
gets a random integer list

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import generate_integer_list

numvalues = int(input("Number of values: "))
low_v = int(input("Low value: "))
high_v = int(input("High value: "))

values = generate_integer_list(numvalues, low_v, high_v)

print("Values: {}".format(values))
