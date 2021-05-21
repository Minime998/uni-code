"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2021-01-21"
-------------------------------------------------------
"""
# [import statements]

# [constants]
PLAINTEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    if year % 4 == 0 and year % 400 == 0:
        leap_year = True
    
    return leap_year


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    values = list(dict.fromkeys(values))
    return


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    for items in range(len(a[0])):
        row = []
        for item in a:
            row.append(item[items])
        b.append(row)
    return b


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = [[sum(x * y for x, y in zip(a_row, b_col)) for b_col in zip(*b)] for a_row in a]
    
    return c


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    line = fv.readline()
    w = 0
    d = 0
    u = 0
    l = 0
    r = 0
    while line != "":
        w += line.count(" ") + line.count("\n")
        linelist = line.strip().split(" ")
        for words in linelist:
            for char in words:  # are ya winning son?
                if char.isdigit():
                    d += 1
                elif char.islower():
                    l += 1
                elif char.isupper():
                    u += 1
                elif char.islower() == False and char.isupper() == False and type(char) == str:
                    r += 1
                
        line = fv.readline()
    
    return u, l, d, w, r


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    for i in "aeiouAEIOU":
        s = s.replace(i, "")
    out = s
    return out


def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ""
    for x in range(len(string)):
        for y in range(len(PLAINTEXT)):
            if string[x].upper() == PLAINTEXT[y]:
                estring += ciphertext[y]
    return estring


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ""
    for x in range(len(string)):
        for y in range(len(PLAINTEXT)):
            if string[x].upper() == PLAINTEXT[y]:
                if y + n < len(PLAINTEXT):
                    estring += PLAINTEXT[y + n]
    return estring

