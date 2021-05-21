'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-25"

'''
from functions import fed_tax, prov_tax

income = int(input("Enter your income: "))
prov_result = prov_tax(income)
fed_result = fed_tax(income)

total_tax = fed_result+prov_result

print("""Federal tax: ${:.2f}
Provincial tax: ${:.2f}
Total tax: ${:.2f}""".format(fed_result,prov_result,total_tax))