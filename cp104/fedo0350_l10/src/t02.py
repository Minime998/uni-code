'''
check for the right id number and give info

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import customer_by_id

id_number = input("enter an ID: ")

fh =open("customers.txt", 'r')
result = customer_by_id(fh, id_number)
print(result)
fh.close()
