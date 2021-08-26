"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-15"
-------------------------------------------------------
"""
# [import statements]

# [constants]


def read_positive():
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
    entlist = []
    num = int(input("Enter a positive number: "))
    while num != 0:
        if num > 0:
            entlist.append(num)
        num = int(input("Enter a positive number: "))
    return entlist


def find_target(entlist, target):
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
    try:
        result = [i for i, x in enumerate(entlist) if x == target]
    except:
        result = []

    return result


def largest_odd(entlist):
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
    lar_odd = -1
    size = len(entlist)
    for index in range(size):
        item = entlist[index]
        if item % 2 != 0:
            lar_odd = item
    return lar_odd


def reverse_list(entlist):
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
    rev_list = []
    size = len(entlist)
    for index in reversed(range(size)):
        item = entlist[index]
        rev_list.append(item)
    print("List reversed: {}".format(rev_list))

    return
