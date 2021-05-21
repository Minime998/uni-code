"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-05"
-------------------------------------------------------
"""
#[import statements]

#[constants]
TAX_RATE = 3.625
OVERTIME = 40
OVERTIME_RATE = 1.5

def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    check_one = 1
    check_two = -1
    while check_one < target:
        check_two += 1
        check_one = 2**check_two
    power = check_one
    return power

def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    check_one = 0
    check_two = 0
    while check_one <= target:
        check_two += 1
        check_one += check_two**2
    final = check_one
    return final

def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """
    num = int(input("First value (-999 to quit): "))
    negatives = 0
    zeros = 0
    positives = 0
    while num != -999:
        if num < 0:
            negatives +=1
        elif num == 0:
            zeros +=1
        else:
            positives +=1
        num = int(input("Next value (-999 to quit): "))
    return negatives, zeros, positives

def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    expenses = 0
    expense = float(input("Enter an expense (0 to quit): "))
    while expense != 0:
        expenses += expense
        expense = float(input("Enter another expense (0 to quit): "))
    balance = available - expenses
    if balance == 0:
        status = "Balanced"
    elif balance > 0:
        status = "Surplus"
    else:
        status = "Deficit"
    return expenses, balance, status

def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    emp_id = int(input("Employee ID: "))
    num_emps = 0
    net_pay = 0
    total = 0
    while emp_id != 0:
        hour_wage_rate = int(input("Hourly wage rate: "))
        hours_worked = int(input("Hours worked: "))
        num_emps += 1
        if hours_worked > OVERTIME:
            net_pay = ((hours_worked-OVERTIME)*(hour_wage_rate*OVERTIME_RATE)+(OVERTIME*hour_wage_rate))*(0.01*(100-TAX_RATE))
            print("Net payment for employee {}: ${:,.2f}".format(emp_id,net_pay))
        else:
            net_pay = (hours_worked*hour_wage_rate)*(0.01*(100-TAX_RATE))
            print("Net payment for employee {}: ${:,.2f}".format(emp_id,net_pay))
        total += net_pay
        emp_id = int(input("Enter next employee ID: "))
    average = total/num_emps
    return total,average


        
        

        

        
    
    
