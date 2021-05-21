'''
the number of flyer per volunteers and the flyers left over

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-09-24"

'''
#Inputs
number_of_flyers = int(input("Number of flyers:"))
number_of_volunteers = int(input("Number of volunteers:"))

#Calculations
flyers_per_volunteer = number_of_flyers//number_of_volunteers
flyers_left_over = number_of_flyers%number_of_volunteers

#Outputs
print("Flyers per volunteer:", flyers_per_volunteer)
print("Flyers left over:", flyers_left_over)
