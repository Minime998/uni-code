'''
sees if a number is divisible by two others

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-22"

'''
from functions import is_divisible

n_number = int(input("Enter number to check for divisibility: "))
i_number = int(input("Enter first value to divide by: "))
j_number = int(input("Enter second number to divide by: "))

result = is_divisible(n_number,i_number,j_number)

if result is True:
    print("{} is evenly divisible by {} and {}".format(n_number,i_number,j_number))
elif result is False:
    print("{} is not evenly divisible by {} and {}".format(n_number,i_number,j_number))