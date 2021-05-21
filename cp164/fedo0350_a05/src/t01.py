'''
test stuff

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-02-25"

'''
from List_array import List
from Sorted_List_array import Sorted_List

source0 = []
source1 = [1, 2, 4, 5, 6, 7, 8, 9, 10]
source2 = []

llist0 = Sorted_List
i = len(source0)
while i != 0:
    llist0.append(source0.pop(0))
    i = i - 1
print(llist0._values)

llist1 = List()
i = len(source1)
while i != 0:
    llist1.append(source1.pop(0))
    i = i - 1
print(llist1._values)

llist2 = List()
i = len(source2)
while i != 0:
    llist2.append(source2.pop(0))
    i = i - 1
print(llist2._values)

