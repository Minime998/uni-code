'''
formats date

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-18"

'''
from functions import convert_date

date_int = int(input("Enter a fate in the format MMDDYYYY: "))

day, month, year = convert_date(date_int)

print("{}/{:02d}/{}".format(day, month, year))
