'''
finds the lowest, higest, total, and average of a list

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import list_stats

values = [94.3,21.5,34.8,100.1]

smallest, largest, total, average = list_stats(values)
print("""Smallest value: {}
Largest value: {}
Total: {}
Average: {}""".format(smallest,largest,total,average))