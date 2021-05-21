'''
linked radix sort

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-04-08"

'''
from List_linked import List
from Sorts_List_linked import Sorts

a = List()

for x in [23, 533, 329, 12, 953]:
    a.append(x)

Sorts.radix_sort(a)
sort = Sorts.sort_test(a)
print(sort)
