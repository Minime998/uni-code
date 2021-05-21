'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-03-11"

'''
from List_linked import List
source = List()
source1 = List()
source1.append(1)
source1.append(1)
source1.append(1)
source2 = List()
source2.append(2)
source2.append(2)
source2.append(2)
source.combine(source1, source2)
for x in source:
    print(x)
