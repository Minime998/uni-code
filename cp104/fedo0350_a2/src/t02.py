'''
Date formatting

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-02"

'''
#import
from datetime import datetime

#input
unform_date = int(input("Enter a date in the format MMDDYYYY: "))

#calculations
form_date = datetime.strptime(str(unform_date), '%m%d%Y').strftime('%d/%m/%Y')

#output
print(form_date)
