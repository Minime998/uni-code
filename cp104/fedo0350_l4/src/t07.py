'''
total amount of change

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-08"

'''
from functions import total_change

num_of_nics = int(input("Enter number of nickels: "))
num_of_dimes = int(input("Enter number of dimes: "))
num_of_quars = int(input("Enter number of quarters: "))
num_of_loons = int(input("Enter number of loonies: "))
num_of_toons = int(input("Enter number of toonies: "))

total = total_change(num_of_nics, num_of_dimes,
                     num_of_quars, num_of_loons, num_of_toons)

print("total amount: ${:.2f}".format(total))
