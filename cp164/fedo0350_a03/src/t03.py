'''
stuff

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-02-04"

'''
from Stack_array import Stack
from functions import stack_reverse

nums = [1, 2]
source = Stack()
i = len(nums)
while i != 0:
    source.push(nums[i - 1])
    nums.pop(i - 1)
    i -= 1
print(source._values)
stack_reverse(source)
print(source._values)
