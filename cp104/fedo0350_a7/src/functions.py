"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-22"
-------------------------------------------------------
"""
#[import statements]

#[constants]

def driver_license(right_list, student_list):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    cor_count = 0
    incor_count = 0
    wrong_list = []
    for i in range(len(right_list)):
        if right_list[i] == student_list[i]:
            cor_count += 1
        else:
            incor_count += 1
            wrong_list.append(i)
    return cor_count, incor_count, wrong_list

def sum_digit(my_str):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    total = 0
    for i in my_str:
        total += int(i)
    
    return total

def find_frequent(my_str):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    counter = 0
    item = my_str[0]
    
    for i in my_str:
        currence = my_str.count(i)
        if currence > counter:
            counter = currence
            item = i
    
    return item 

def add_spaces(my_str):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    sentence = []
    
    sentence.append(my_str[0])
    for char in my_str[1:]:
        if char.islower():
            sentence.append(char)
        elif char.isupper():
            sentence.append(" ")
            sentence.append(char.lower())
    result = ''.join(sentence)
    
    return result 

def is_chain(words_list):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    result = True
    if words_list[0][-1] != words_list[1][1]:
        result = False
    
    return result
    
    
    
    
    
        
    
        
    
    
        
    
    
    
