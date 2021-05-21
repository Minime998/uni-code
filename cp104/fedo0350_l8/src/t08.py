'''
searches a list for a value

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import linear_search
a = [10, 76, 54, 78, 291, 87, 12, 5, 489, 6, 66, 28]
v = int(input("Value to input: "))

index = linear_search(a, v)

print("Index of {}: {}".format(v,index))
