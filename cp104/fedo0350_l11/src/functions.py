"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-12-03"
-------------------------------------------------------
"""
#[import statements]
import random
#[constants]

def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    if value_type == 'float':
        matrix = [[random.uniform(low,high) for x in range(cols)] for x in range(rows)]
    else:
        matrix = [[random.randint(low,high) for x in range(cols)] for x in range(rows)] 
    
    return matrix

def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    cols = len(matrix[0])
    count = 0
    if value_type == "float":
        for x in range(cols):
            print("{:4}".format(x), end =" ")
        print("")
        if value_type == "float":
            for row in matrix:
                print(count, end = " ")
                for val in row:
                    print('{:4.2f}'.format(val),end = " ")
                count +=1
                print("")
    if value_type == "int":
        for x in range(cols):
            print("{:4}".format(x), end =" ")
        print("")
        if value_type == "int":
            for row in matrix:
                print(count, end = "")
                for val in row:
                    print('{:4}'.format(val),end = "")
                count+=1
                print("")
        

    return

def stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    count = 0
    
    total = sum(map(sum, matrix))

    for lists in matrix:
        for nums in lists:
            if nums < smallest:
                smallest = nums
            if nums > largest:
                largest = nums
            count += 1
    
    average = total/count
    
    
    return smallest, largest, total, average

def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    count = 0
    
    for row in matrix:
        for b in row:
            if b == char:
                count +=1
    return count

def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of ?)
        matrix2 - the second matrix (2D list of ?)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    return
        
    
    

