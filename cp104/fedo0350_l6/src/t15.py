'''
gives the min max total and average for a set of numbers in num

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-29"

'''
from functions import statistics

num = int(input("Enter number of values: "))

minum, maxum, total, average = statistics(num)

print("""Minimum: {:.2f}
Maximum: {:.2f}
Total: {:.2f}
Average: {:.2f}""".format(minum, maxum, total, average))
