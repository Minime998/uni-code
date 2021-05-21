'''
circular test

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-02-11"

'''
from Queue_circular import Queue

target = Queue()
target.insert(1)
print(target._values)
v = target.peek()
print(v)
print(target._values)
v = target.remove()
print(target._values)
v = target.is_empty()
print(v)

