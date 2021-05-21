'''
finds the smallest largest total average

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import number_stats

fh = open("numbers.txt","r")

smallest, largest, total, average = number_stats(fh)

print("""Smallest: {} 
Largest: {} 
Total: {:.2f}
Average: {:.2f}""".format(smallest,largest,total,average))
fh.close()