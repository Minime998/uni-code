'''
program description

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import find_target
from functions import read_positive

entlist = read_positive()
target = int(input("target: "))

target_loc = find_target(entlist, target)

print("target exists at location {}".format(target_loc))