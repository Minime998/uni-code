'''
driver test scores

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-04-20"

'''
from functions import driver_license

right_list = ["A", "C", "A", "A", "D", "B", "C", "A", "C",
              "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
answers = input("""Enter a sequence of 20 choices seperated by a space, each A-D in 
Uppercase: """)
student_list = answers.split()

cor_list, incor_list, wrong_list = driver_license(right_list, student_list)

if cor_list >= 15:
    print("You passed your driver license exam")
print("""#Correct answers = {} ,# incorrect answers = {}
A list of incorrectly answered questions = {}
To pass the exam you need to score 15 out of 20""".format(cor_list, incor_list, wrong_list))
