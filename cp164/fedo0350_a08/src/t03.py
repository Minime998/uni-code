'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-03-25"

'''

from BST_linked import BST
from Letter import Letter
from functions import letter_table, do_comparisons, DATA3

pop_bst = BST()

for x in range(len(DATA3)):
    pop_bst.insert(Letter(DATA3[x]))

file_v = open("miserables.txt", "r")
do_comparisons(file_v, pop_bst)
file_v.close()
letter_table(pop_bst)
