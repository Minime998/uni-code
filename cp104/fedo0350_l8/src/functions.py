"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-12"
-------------------------------------------------------
"""
#[import statements]
from random import randint

#[constants]

def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    return digits[n] 

def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = []
    for nums in range(0,n):
        x = randint(low,high)
        values.append(x)
    
    return (values)

def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    total = values[0]
    smallest = values[0]
    largest = values[0]
    
    for x in values[1:]:
        if x < smallest:
            smallest = x
        else:
            if x > largest:
                largest = x
        total = total+x
    average = total/len(values)
        
    return smallest, largest, total, average

def linear_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns its index.
    Use: index = linear_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        index - the index of the location of v in a, -1 if not found (int).
    -------------------------------------------------------
    """
    index = -1
    index_counter = 0
    value = 0
    while index_counter != index:
        for value in a:
            if v != value:
                index_counter += 1
            elif v==value:
                index = index_counter
        index_counter = index
    return index

def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sum(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    for x in range(0,len(source1)):
        target.append(source1[x]+source2[x])
    
    return target
        
        




        
    
  
    
    

