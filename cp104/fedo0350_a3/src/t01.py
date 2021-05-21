'''
takes a object's falling time and gives the distance it has fallen

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-18"

'''

from functions import falling_distance

time_falling = int(input("Enter the time (in secs): ")) 

object_fall = falling_distance(time_falling)

print("The Object has falling {:.2f} meters in {} seconds.".format(object_fall,time_falling))