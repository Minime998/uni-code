'''
slant height area and vol of a square pyramid

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-08"

'''
from functions import square_pyramid

len_of_base = float(input("Length of base: "))
perp_height_of_triangle = float(input("Perpendicular height of pyramid: "))

sh, area, vol = square_pyramid(len_of_base, perp_height_of_triangle)

print("""Slant height of square pyramid: {:.2f}
Area of square pyramid: {:.2f}
Volume of square pyramid: {:.2f}""".format(sh,area,vol))
