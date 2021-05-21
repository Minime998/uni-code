'''
The value of compound interest

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-09-26"

'''
principal = int(input("Principal: "))
interest = float(input("Interest (decimal): "))
num_of_years = int(input("Number of years: "))
comp_interst_per_year = int(input("Compound interest per year: "))

amount_accumulated = principal*(1+interest/comp_interst_per_year)**(comp_interst_per_year*num_of_years)

print("Balance: ${0:.2f}".format(amount_accumulated))