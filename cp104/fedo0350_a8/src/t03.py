'''
gets the info on a file

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import file_analysis

fh = open("text.txt", 'r')
uppercount, lowercount, digitcount, whitecount = file_analysis(fh)

print("""Uppercount: {}
Lowercount: {}
Digitcount: {}
Whitecount: {}""".format(uppercount, lowercount, digitcount, whitecount))
fh.close()

fh = open("output_t03.txt", 'w')
fh.write("""Upper count: {}
Lowercount: {}
Digitcount: {}
Whitecount: {}""".format(uppercount, lowercount, digitcount, whitecount))
fh.close()
