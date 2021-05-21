'''
parses a product code

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import parse_code

product_code = input("Enter a product code: ")

pc, pi, pq = parse_code(product_code)

print("""Category: {}
ID: {}
Qualifier: {}""".format(pc,pi,pq))
