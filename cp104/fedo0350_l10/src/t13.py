'''
copy stuff to new file 

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import file_copy

fh_1 = open("words.txt", 'r')
fh_2 = open("new_words.txt", 'w')

print("Copying 'words.txt' to 'new_words.txt'")
file_copy(fh_1, fh_2)
fh_1.close()
fh_2.close()
