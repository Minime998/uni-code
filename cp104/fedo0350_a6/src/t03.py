'''
program description

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import largest_odd
from functions import read_positive

entlist = read_positive()
lar_odd = largest_odd(entlist)

print("Largest odd: {}".format(lar_odd))