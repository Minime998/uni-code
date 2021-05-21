"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-08"
-------------------------------------------------------
"""
#[import statements]

#[constants]

def perfect_square(num):
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
    if num >= 0:
        print("Perfect square below {} are: ".format(num), end ='')
        for x in range(1,num):
            if (x**0.5)**2 ==x:
                print(x,"", end = '')
                
    else:
        print("Error: you entered a negative number")
        
    return

def factorial(num):
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
    fact = 1
    for x in range(1,num+1):
        fact = fact*x
    return fact

def is_prime(num):
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
    i = 2
    toggle = 0
    while i < num:
        if num%i == 0:
            toggle = 1
            result = False
        i = i+1
    if toggle == 0:
        result = True
            
        
    return result

def print_pattern(num_rows):
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
    for r in range(num_rows+1):
        for c in range(r):
            print("#", end='')
        print('')
        
    return

def winner():
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
    team = input("Enter the winning team: ")
    red_counter = 0
    green_counter = 0
    while team != "":
        if team == "red":
            red_counter += 1
        elif team == "green":
            green_counter += 1
        team = input("Enter the winning team: ")
    
    return green_counter, red_counter
        
    
    
    
        
    

