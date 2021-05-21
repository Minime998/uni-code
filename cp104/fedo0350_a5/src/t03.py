'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import is_prime

num = int(input("Enter a positive integer number: "))

if num >=0:
    result = is_prime(num)
    if result == True:
        print("{} is a prime number".format(num))
    else:
        print("{} is not a prime number".format(num))
else:
    print("Error: you entered a negative number")