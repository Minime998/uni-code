'''
Profit from total sales

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-02"

'''
# constant
Annual_Profit = 0.23

# inputs
total_sales = float(input("Total sales: "))

# calculations
profit = Annual_Profit*total_sales
Annual_Profit *= 100

# outputs
print("""Projected Profit Report
{:->26}
Total sales: $ {:.2f}
Annual profit: % {:.0f}
{:->26}
Profit: $ {:.2f}""".format("-", total_sales, Annual_Profit, "-", profit))
