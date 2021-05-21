'''
Matrix multiply

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-01-21"

'''
from functions import matrixes_multiply

a = [[12, 7, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]
b = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1], [7, 8, 9, 2]]

c = matrixes_multiply(a, b)
print(c)
