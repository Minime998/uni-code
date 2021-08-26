'''
gets the median from a file

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import locate_median

fh = open("numbers.txt", 'r')

median = locate_median(fh)

print("Median is {}".format(median))
fh.close()

fh = open("output_t02.txt", 'w')
fh.write(str(median))
fh.close()
