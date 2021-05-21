'''
Total cubic meters with amounts lined up

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-01"

'''
#inputs
dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

#calculations
total = dirt+gravel+sand

#outputs
print("""Material   Cubic Metres
Dirt {:>10}
Gravel {:>8}
Sand {:>11}
Total {:>10.1f}""".format(dirt,gravel,sand,total))