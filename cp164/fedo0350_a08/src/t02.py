'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-03-25"

'''
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total, DATA1, DATA2, DATA3

seperator = "-" * 30

order_bst = BST()
split_bst = BST()
popular_bst = BST()

for i in range(len(DATA1)):
    order_bst.insert(Letter(DATA1[i]))
    split_bst.insert(Letter(DATA2[i]))
    popular_bst.insert(Letter(DATA3[i]))

file_v = open("miserables.txt", "r")

do_comparisons(file_v, order_bst)
order_com = comparison_total(order_bst)
do_comparisons(file_v, split_bst)
split_com = comparison_total(split_bst)
do_comparisons(file_v, popular_bst)
pop_com = comparison_total(popular_bst)

file_v.close()

print("For '{}':".format("miserables.txt"))
print()
print("Comparing by order: {}".format(DATA1))
print("Total Comparisons: {:,}".format(order_com))
print(seperator)
print("Comparing by order: {}".format(DATA2))
print("Total Comparisons: {:,}".format(split_com))
print(seperator)
print("Comparing by order: {}".format(DATA3))
print("Total Comparisons: {:,}".format(pop_com))
