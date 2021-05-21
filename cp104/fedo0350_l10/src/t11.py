'''
finds the last longest word

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import find_longest

fh = open("words.txt","r")

word = find_longest(fh)

print("'{}' is the last longest word".format(word))
fh.close()
