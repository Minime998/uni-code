'''
stuff

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-02-04"

'''
from Stack_array import Stack
from functions import stack_split_alt

nums = [1, 2]
source = Stack()
i = len(nums)
while i != 0:
    source.push(nums[i - 1])
    nums.pop(i - 1)
    i -= 1
print(source._values)
target1, target2 = stack_split_alt(source)
print(source._values)
print(target1._values)
print(target2._values)
