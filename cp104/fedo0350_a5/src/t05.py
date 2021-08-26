'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import winner

green_counter, red_counter = winner()

if green_counter == red_counter:
    win = "tie"
elif green_counter > red_counter:
    win = "green wins"
else:
    win = "red wins"

print("""Number of red entered: {}
number of green entered: {}
{}""".format(red_counter, green_counter, win))
