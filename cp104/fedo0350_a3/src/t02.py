'''
calculates total calories from carbs and fats

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-11-18"

'''

from functions import calorie_calculator

fat_grams = int(input("Enter the fat grams consumed: "))
carb_grams = int(input("input Enter the carbohydrate grams consumed: "))

cals_from_fat, cals_from_carbs = calorie_calculator(fat_grams, carb_grams)

total_cals = cals_from_fat+cals_from_carbs

print("""Fat calories: {}
Carb calories: {}
Total calories: {}""".format(cals_from_fat,cals_from_carbs,total_cals))