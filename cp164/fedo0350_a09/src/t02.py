'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-04-01"

'''
from Hash_Set_sorted import Hash_Set
from functions import insert_words, comparison_total

hash_set = Hash_Set(20)
fv = open("miserables.txt", 'r')
insert_words(fv, hash_set)

total, max_word = comparison_total(hash_set)

print("""Using array-based Sorted List Hash_Set
Total Comparisons: {}
Word with maximum comparisons {}""".format(total, max_word))
