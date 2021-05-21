'''
inner split pq

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-02-11"

'''
from Priority_Queue_array import Priority_Queue
source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pq = Priority_Queue()
i = len(source)
while i != 0:
    pq.insert(source.pop(0))
    i = i - 1
print(pq._values)

target1, target2 = pq.split_key(5)
print(target1._values)
print(target2._values)
print(pq._values)
