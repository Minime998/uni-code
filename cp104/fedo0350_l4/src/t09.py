'''
 calculate and returns fraction values

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-08"

'''
from functions import fraction_product

first_num = int(input("Enter numerator of fraction 1: "))
first_den = int(input("Enter denominator of fraction 1: "))
second_num = int(input("Enter numerator of fraction 2: "))
second_den = int(input("Enter denominator of fraction 2: "))

num, den, product = fraction_product(
    first_num, first_den, second_num, second_den)

print("""Product = {}/{}
Decimal = {:.2f}""".format(num, den, product))
