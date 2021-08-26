"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-10-25"
-------------------------------------------------------
"""
# [import statements]

# [constants]


def pieces_produced(time, num_workers):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Parameters:
        [parameter name - parameter description (parameter type and constraints)]
   Returns:
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    if time in range(6, 11):
        pieces_made = num_workers*30
    elif time in range(10, 15):
        pieces_made = num_workers*40
    elif time in range(14, 19):
        pieces_made = num_workers*35
    else:
        pieces_made = -1

    return pieces_made


def num_day(day_num):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Parameters:
        [parameter name - parameter description (parameter type and constraints)]
   Returns:
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    if day_num in range(1, 8):
        if day_num == 1:
            result = "Monday"
        elif day_num == 2:
            result = "Tuesday"
        elif day_num == 3:
            result = "Wednesday"
        elif day_num == 4:
            result = "Thursday"
        elif day_num == 5:
            result = "Friday"
        elif day_num == 6:
            result = "Saturday"
        elif day_num == 7:
            result = "Sunday"
    else:
        result = "Error"

    return result


def fed_tax(income):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Parameters:
        [parameter name - parameter description (parameter type and constraints)]
   Returns:
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    if income <= 35000:
        fed_result = income*0.15
    elif income > 35000 and income <= 100000:
        fed_result = (35000*0.15)+((income-35000)*0.25)
    else:
        fed_result = (35000*0.15)+(65000*0.25)+((income-100000)*0.35)

    return fed_result


def prov_tax(income):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Parameters:
        [parameter name - parameter description (parameter type and constraints)]
   Returns:
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    if income > 50000:
        prov_result = (income-50000)*0.05
    else:
        prov_result = 0

    return prov_result


def pocket_colour(col):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Parameters:
        [parameter name - parameter description (parameter type and constraints)]
   Returns:
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    if col == 0:
        result = "green"
    elif col in range(1, 11):
        if col % 2 == 0:
            result = "black"
        else:
            result = "red"
    elif col in range(11, 19):
        if col % 2 == 0:
            result = "red"
        else:
            result = "black"
    elif col in range(19, 29):
        if col % 2 == 0:
            result = "black"
        else:
            result = "red"
    elif col in range(29, 37):
        if col % 2 == 0:
            result = "red"
        else:
            result = "black"
    else:
        result = "Error"

    return result


def colour_mix(pri, sec):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Parameters:
        [parameter name - parameter description (parameter type and constraints)]
   Returns:
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    if (pri == "red" or pri == "blue") and (sec == "blue" or sec == "red"):
        result = "purple"
    elif (pri == "red" or pri == "yellow") and (sec == "yellow" or sec == "red"):
        result = "orange"
    elif (pri == "blue" or pri == "yellow") and sec == ("yellow" or sec == "blue"):
        result = "green"
    else:
        result = "Error"

    return result
