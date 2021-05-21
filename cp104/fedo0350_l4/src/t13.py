'''
fahrenheit to celsius

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-08"

'''

from functions import f_to_c

fahren = int(input("Enter a temperature (f): "))

celsius = f_to_c(fahren)

print("{:.0f} F = {:.0f} C".format(fahren,celsius))

