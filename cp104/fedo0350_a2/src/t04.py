'''
Divide number of balloons at party
Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-02"

'''
# inputs
num_of_balloons = int(input("Number of balloons: "))
num_of_children = int(input("Number of Children: "))

# calculations
will_receieve = num_of_balloons//num_of_children
wont_receieve = num_of_balloons % num_of_children

# outputs
print("""Each child will receieve {} balloons
Balloons that will not be distributed: {}""".format(will_receieve, wont_receieve))
