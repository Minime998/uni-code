'''
get all the data

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-01-21"

'''
from functions import file_analyze

fv = open("text.txt", 'r')

u, l, d, w, r = file_analyze(fv)

print(u, l, d, w, r)
