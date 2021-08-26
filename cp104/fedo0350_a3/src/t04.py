'''
convert seconds to days, hours, mins, and secs

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-18"

'''
from functions import convert_sec

num_sec = int(input("Enter number of seconds: "))

days, hours, minutes, seconds = convert_sec(num_sec)

print("There are {} days, {} hours, {} minutes, and {} seconds in {} seconds.".format(
    days, hours, minutes, seconds, num_sec))
