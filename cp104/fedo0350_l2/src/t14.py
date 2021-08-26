'''
what is required for making mac and cheese

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-09-24"

'''
# Constants
milk = 4
butter = 8
flour = 0.5
salt = 2

# Inputs
servings_of_mac = int(input("Enter servings of Mac & Cheese:"))

# Calculations
real_serving = 6/servings_of_mac
real_milk = milk/real_serving
real_butter = butter/real_serving
real_flour = flour/real_serving
real_salt = salt/real_serving

# Outputs
print("{0} servings of Mac & Cheese:".format(servings_of_mac))
print("milk (cups): {0:.2f}".format(real_milk))
print("butter (tablespoons): {0:.2f}".format(real_butter))
print("flour (cups): {0}".format(real_flour))
print("salt (teaspoons): {0:.2f}".format(real_salt))
