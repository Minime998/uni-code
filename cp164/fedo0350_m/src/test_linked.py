# Imports
from Set_linked import Set
# Constants
SEP = '_' * 40
# Testing
source = Set()
print(SEP)
empty = source.is_empty()
print("Set is empty: {}".format(empty))
length = len(source)
print("Set length: {}".format(length))
print(SEP)
print("Add values 0 - 5")
for i in range(6):
    source.add(i)
empty = source.is_empty()
print("Set is empty: {}".format(empty))
length = len(source)
print("Set length: {}".format(length))
print("Values in set:")
for v in source:
    print(v)
print(SEP)
print("Attempt to add a value already in set (1)")
added = source.add(1)
print("Added: {}".format(added))
print(SEP)
print("Remove 3")
removed = source.remove(3)
print("Removed:", removed)
print("Values in set:")
for v in source:
    print(v)
print(SEP)
print("Remove Front")
removed = source.remove_front()
print("Removed:", removed)
print("Values in set:")
for v in source:
    print(v)
