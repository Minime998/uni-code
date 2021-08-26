'''
Calculates the number of days and hours and mins

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-01"

'''
# constant
Min_HOUR = 60

# inputs
min_to_convert = int(input("Enter number of minutes: "))

# calculations
day_calc = min_to_convert/1440
hrs_calc = (min_to_convert % (24*60))//60
min_calc = min_to_convert % Min_HOUR

# outputs
print("There are {:.0f} days, {:.0f} hours, and {:.0f} minutes in {:.0f} minutes".format(
    day_calc, hrs_calc, min_calc, min_to_convert))
