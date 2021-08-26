'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-03-08"

'''
from List_linked import List
source = List()
source.append(12)
source.append(13)
source.append(14)
source.append(15)
source.append(16)
source.append(17)
for x in source:
    print(x)

source2 = List()
source2.append(12)
source2.append(13)
source2.append(14)
source2.append(15)
source2.append(16)
source2.append(17)

b = source.is_identical_r(source2)
print(b)

source.reverse_r()
for x in source:
    print(x)
