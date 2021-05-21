'''
is the queue the same?

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-02-11"

'''
from Queue_array import Queue
from functions import queue_is_identical
queue1 = Queue()
queue2 = Queue()
source1 = [1, 2, 3, 4, 5, 6]
source2 = [2, 4, 5, 7, 8, 9]
i = len(source1)
while i != 0:
    queue1.insert(source1.pop(0))
    i = i - 1
i = len(source2)
while i != 0:
    queue2.insert(source2.pop(0))
    i = i - 1
ident = queue_is_identical(queue1, queue2)
print(ident)
print(queue1._values)
print(queue2._values)
