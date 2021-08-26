'''
gets the list and sum of nums from a file

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import total_nums

fh = open("text_numbers.txt", 'r')

numlist, total = total_nums(fh)

print("""All nums: {}
Sum of all nums: {}""".format(numlist, total))
fh.close()

fh = open("output_t01.txt", 'w')
fh.write("List of nums:")
for x in range(len(numlist)):
    fh.write(str(numlist[x])+" ")
fh.write("\n")
fh.write("Total of nums:"+str(total))
fh.close()
