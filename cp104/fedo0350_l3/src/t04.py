'''
Print discount from float

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-01"

'''
#inputs
number = float(input("Enter number: "))
percent = float(input("Enter percent: "))

#calculations
discounted_price = number*(percent/100)

#outputs
print("A {} percent discount on {:.0f} is {:,.1f}".format(percent,number,discounted_price))