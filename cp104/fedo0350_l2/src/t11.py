'''
projected profit on sales

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-09-24"

'''
#Constants
Profit = 0.18

#Inputs
projected_annual_sales = float(input("Enter projected annual sales:"))

#Calculations
projected_profit = projected_annual_sales*Profit

#Output
print("The projected profit on sales of ${0:,.2f} is ${1:,.2f}.".format(projected_annual_sales,projected_profit))