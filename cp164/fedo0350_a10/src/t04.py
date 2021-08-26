'''
linked Gnome sort

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-04-07"

'''
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts

a = Deque()

a.insert_front(12)
a.insert_front(13)
a.insert_front(2)
a.insert_front(78)
a.insert_front(1)

Sorts.gnome_sort(a)
sort = Sorts.sort_test(a)
print(sort)
