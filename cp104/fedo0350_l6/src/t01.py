'''
takes the sum of all even numbers between 2 and a number

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-29"

'''
from functions import sum_even

num = int(input("Enter a number: "))

total = sum_even(num)

print("The sum of all even numbers from 2 to {} is : {}".format(num,total))