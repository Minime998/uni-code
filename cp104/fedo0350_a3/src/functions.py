"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-18"
-------------------------------------------------------
"""
# [import statements]
import random

# [constants]
GRAVITY = 9.8


def falling_distance(falling_time):
    """
    -------------------------------------------------------
    Takes an objects falling time and returns the the distance the object has been falling.
    Use: object_fall = falling_distance(time_falling)
    -------------------------------------------------------
    Parameters:
        falling_time - falling time of an object (int >= 0)
   Returns:
       distance_fallen - distance the object has fallen (float)
    -------------------------------------------------------
    """
    distance_fallen = 1/2*(GRAVITY*(falling_time**2))

    return distance_fallen


def calorie_calculator(fat_grams, carb_grams):
    """
    -------------------------------------------------------
    Takes fat grams and carb grams and returns the calorie count
    Use: cals_from_fat, cals_from_carbs = calorie_calculator(fat_grams, carb_grams)
    -------------------------------------------------------
    Parameters:
        fat_grams - the grams of fat (int >= 0)
        carb_grams - the grams of carbohydrates (int >= 0)
   Returns:
       cals_from_fat - total calories from fat (int)
       cals_from_carbs - total calories from carbohydrates (int)
    -------------------------------------------------------
    """
    cals_from_fat = fat_grams*9
    cals_from_carbs = carb_grams*4

    return cals_from_fat, cals_from_carbs


def convert_date(date_int):
    """
    -------------------------------------------------------
    converts date_int into days, month and year
    use: day,month,year = convert_date(date_int)
    -------------------------------------------------------
    Parameters:
        date_int - (int > 0)
   Returns:
       day: the day in the month in date_int (int >= 0)
       month: the month in date_int (int >= 0)
       year: the years in date_int (int >= 0)
    -------------------------------------------------------
    """
    day = (date_int/10000) % 100
    month = (date_int/1000000) % 100
    year = date_int % 10000

    return int(day), int(month), int(year)


def convert_sec(num_sec):
    """
    -------------------------------------------------------
    converts num sec into days, hours, minutes and seconds
    use: days,hours,minutes, seconds = convert_sec(num_sec)
    -------------------------------------------------------
    Parameters:
        num_sec - (int > 0)
   Returns:
       days: number of days in num_sec (int >= 0)
       hours: number of hours in num_sec (int >= 0)
       minutes: number of minutes in num_sec (int >= 0)
       seconds: number of seconds in num_sec (int >= 0)
    -------------------------------------------------------
    """
    days = num_sec/86400
    hours = (num_sec % 86400)//3600
    minutes = num_sec//3600
    seconds = num_sec % 60

    return int(days), int(hours), int(minutes), int(seconds)


def math_quiz():
    """
    -------------------------------------------------------
    gives out two random integers so the user can input a guess
    Use: math_quiz()
    -------------------------------------------------------
    Parameters:
        none
   Returns:
       none
    -------------------------------------------------------
    """
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)

    total_num = num1+num2

    print("""{:>-9}
    + {}""".format(num1, num2))

    guess_ans = int(input("Enter answer:"))

    print("Your answer: {}, it should be: {}".format(guess_ans, total_num))
