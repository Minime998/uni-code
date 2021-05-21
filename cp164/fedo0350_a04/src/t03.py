'''
inter identical

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-02-11"

'''
from Queue_array import Queue
queue1 = Queue()
queue2 = Queue()
source1 = [1, 2, 3, 4]
source2 = [1, 2, 3, 4]
i = len(source1)
while i != 0:
    queue1.insert(source1.pop(0))
    i = i - 1
i = len(source2)
while i != 0:
    queue2.insert(source2.pop(0))
    i = i - 1
v = queue1.is_identical(queue2)
print(v)
