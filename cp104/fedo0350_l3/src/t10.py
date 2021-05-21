'''
year/moth/day format

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-01"

'''
#inputs
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

#outputs
print("The date: {}/{:02d}/{:02d}".format(year,month,day))