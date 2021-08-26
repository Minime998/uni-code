'''
appends to file

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import customer_append

fields = ['35612', 'David', 'Brown', '237.56', '2008-10-10']

fh = open("customers.txt", 'a')

customer_append(fh, fields)
fh.close()
