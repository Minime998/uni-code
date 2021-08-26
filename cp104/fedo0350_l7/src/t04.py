'''
gives the sum of squares closest to, and greater thean 
or equal to, a target

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-05"

'''
from functions import sum_squares

target = int(input("Enter a target number: "))
final = sum_squares(target)
print("Sum of squares >= target {} is {}".format(target, final))
