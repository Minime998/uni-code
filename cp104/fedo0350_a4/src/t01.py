'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-25"

'''
from functions import pieces_produced

time = int(input("Time of the day: "))
num_workers = int(input("Number of workers: "))

pieces_made = pieces_produced(time, num_workers)

if pieces_made != -1:
    print("The total number of pieces produced: {}".format(pieces_made))
else:
    print("Can not perform the calculations")
