'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import power_of_two
target = int(input("Enter target number: "))
power = power_of_two(target)
print("The closest power of 2 >= {} is {}".format(target,power))
