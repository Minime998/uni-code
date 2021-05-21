'''
gets the categories of entered nums

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-05"

'''
from functions import num_categories

negatives, zeros, positives = num_categories()

print("""Number of negative values: {}
Number of zeroes: {}
Number of positive values: {}""".format(negatives,zeros,positives))
