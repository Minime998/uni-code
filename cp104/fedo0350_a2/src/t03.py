'''
Sum of two digits

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-02"

'''
#inputs
num_n = int(input("Enter a positive two digit number: "))

#calculations
sum_of_digits = sum(int(digit) for digit in str(num_n))

#outputs
print("The sum of the two digits is: {}".format(sum_of_digits))
