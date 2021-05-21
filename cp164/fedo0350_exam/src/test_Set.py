"""
-------------------------------------------------------
Simple Set testing - Exam
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
# Imports
from Set_linked import Set

# Constants
SEP = '-' * 60

# Testing
source = Set()

print(SEP)
empty = source.is_empty()
print("Set is empty: {}".format(empty))
length = len(source)
print("Set length: {}".format(length))

print(SEP)
print("Add values 0 (front) - 5 (end)")
for i in range(6):
    source.add(i)

empty = source.is_empty()
print("Set is empty: {}".format(empty))
length = len(source)
print("Set length: {}".format(length))

print("Values in set (front to end):")

for v in source:
    print(v, end=", ")
print()

print(SEP)
print("Attempt to add a value already in set (1)")
added = source.add(1)
print("Added: {}".format(added))

print(SEP)
print("Remove 3")
removed = source.remove(3)
print("Removed:", removed)
print("Values in set (front to end):")

for v in source:
    print(v, end=", ")
print()

print(SEP)
print("Remove Front")
removed = source.remove_front()
print("Removed:", removed)
print("Values in set (front to end):")

for v in source:
    print(v, end=", ")
print()

print(SEP)

# Further testing here
