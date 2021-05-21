'''
add 2d lists

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import add_2d_list
amount = 2
nums_list = []
matrix_nums = (input("Enter 12 numbers pls: "))
str_list = matrix_nums.split(" ")
for x in range(len(str_list)):
    nums_list.append(int(str_list[x]))

matrix1 = [nums_list[spot:spot+amount] for spot in range(0, 5, amount)]

matrix2 = [nums_list[spot:spot+amount] for spot in range(6, 11, amount)]


