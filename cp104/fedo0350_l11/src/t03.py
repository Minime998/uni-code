'''
print out 2d matrix to table

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import print_matrix_num
from functions import generate_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = float(input("Low value: "))
high = float(input("High value: "))
value_type = input("Type of values: ")

matrix = generate_matrix_num(rows, cols, low, high, value_type)

print_matrix_num(matrix, value_type)


