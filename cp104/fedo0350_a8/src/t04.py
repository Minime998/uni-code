'''
validates sn numbers

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import valid_sn_file

fh = open("serial_number.txt", 'r')
oh1 = open("output_t04_valid.txt", 'w')
oh2 = open("ouput_t04_invalid.txt", 'w')

valid_sn_file(fh, oh1, oh2)
fh.close()
oh1.close()
oh2.close()
