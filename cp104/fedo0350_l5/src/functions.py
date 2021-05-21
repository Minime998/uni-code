"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   your fedo0350@mylaurier.ca
__updated__ = "2020-10-22"
-------------------------------------------------------
"""
#[import statements]

#[constants]
OVERTIME = 40
OVERTIME_RATE = 1.5
TAX_RATE = 3.625
MIN_YEARS = 5
MIN_SALARY = 30000

def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    diff1 = abs(target-v1)
    diff2 = abs(target-v2)
    
    if diff1 > diff2:
        result = v2
    elif diff2 > diff1:
        result = v1
    else:
        result = v1
    
    return result

def is_divisible(n, i, j):
    """
    -------------------------------------------------------
    Determines if n is evenly divisible by both i and j.
    Use: result = is_divisible(n, i, j)
    -------------------------------------------------------
    Parameters:
        n - the number to check for divisibility (int)
        i - one of the values to divide n by (int)
        j - another value to divide n by (int)
    Returns:
        result - True if n is evenly divisible by both
            i and j, False otherwise (boolean)
    ------------------------------------------------------
    """
    
    if n%i==0 and n%j==0:
        result = True
    else:
        result = False
    
    return result

def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """
    if hours_worked > OVERTIME:
        net_payment = ((hours_worked-OVERTIME)*(hourly_rate*OVERTIME_RATE)+(OVERTIME*hourly_rate))*(0.01*(100-TAX_RATE))
    else:
        net_payment = (hours_worked*hourly_rate)*(0.01*(100-TAX_RATE)) 

    return net_payment

def richter(intensity):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        intensity - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - description of earthquake damage (str)
    -------------------------------------------------------
    """
    if intensity < 5:
        result = "Little or no damage"
    elif 5<= intensity < 5.5:
        result = "Some damage"
    elif 5.5 <= intensity < 6.5:
        result = "Serious damage: walls may crack or fall"
    elif 6.5 <= intensity < 7.5:
        result = "Disaster: buildings may collapse"
    else:
        result = "Catastrophe: most buildings destroyed"
    
    return result

def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    qualified = False
    if int(input("Years employed: ")) >= MIN_YEARS:
        if float(input("Annual salary: ")) >= MIN_SALARY:
            qualified = True
    
    return qualified