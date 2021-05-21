'''
Cost of dogs groomed in a day

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-09-24"

'''
#Inputs
large_dogs_groomed = int(input("Number of large dogs groomed:"))
small_dogs_groomed = int(input("Number of small dogs groomed:"))

#Calculations
cost_of_large_dogs_groomed = 75.00*large_dogs_groomed
cost_of_small_dogs_groomed = 50.00*small_dogs_groomed
total_earned = cost_of_large_dogs_groomed+cost_of_small_dogs_groomed

#Outputs
print("Total earned for the day: ${0:,.2f}".format(total_earned))
