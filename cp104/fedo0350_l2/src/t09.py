'''
the cost and total cost of all containers

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-09-24"

'''
# Constants
PI = 3.14

# Inputs
diameter_of_container_base = float(input("Diameter of container base (cm):"))
height_of_container = float(input("Height of container (cm):"))
cost_of_material = float(input("Cost of material ($/cm^2):"))
number_of_containers = int(input("Number of containers:"))

# Calculations
container_cost = ((PI*((diameter_of_container_base/2)**2))+(2*PI *
                  height_of_container*(diameter_of_container_base/2)))*cost_of_material
total_cost = container_cost*number_of_containers

# Output
print("The cost of one container: ${0:,.2f}".format(container_cost))
print("The total cost of all containers is ${0:,.2f}".format(total_cost))
