'''
frequency

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import find_frequent

my_str = input("Enter a string: ")

item = find_frequent(my_str)

print("Most frequent characters: {}".format(item))
