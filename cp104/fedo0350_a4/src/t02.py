'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import num_day

day_num = int(input("Please enter a number between 1 and 7: "))

result = num_day(day_num)

print("The number {} corresponds to {}.".format(day_num,result))