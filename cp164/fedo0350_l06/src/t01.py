'''
preannes annpend and insert

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-03-01"

'''
from List_linked import List
llist = List()
newllist1 = []
source = [99, 22, 33, 44, 55]
llist.append(source[0])
llist.append(source[1])
llist.append(source[2])
llist.append(source[3])
llist.append(source[4])
key = 33
n = llist.remove(key)
print(n)
for values in llist:
    newllist1.append(values)
print(newllist1)
newlist2 = []
llist[-1] = -1
for values in llist:
    newlist2.append(values)
print(newlist2)
