'''
draws a rectangle from chars

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-29"

'''
from functions import draw_rectangle

height = int(input("Enter height in characters: "))
width = int(input("Enter width in characters: "))
char = input("Enter the draw character: ")

draw_rectangle(height, width, char)