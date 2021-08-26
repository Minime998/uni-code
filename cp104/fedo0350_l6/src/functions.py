"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-10-29"
-------------------------------------------------------
"""
# [import statements]

# [constants]
RETIREMENT = 65


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for x in range(2, num+1, 2):
        total = total+x
    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, height+1):
        for h in range(1, width+1):
            print(char, end='')
        print()

    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for x in range(n, 1, -1):
        print("""{} bottles of beer on the wall, {} bottles of beer.
        Take one down, pass it around, {} bottles of beer on the wall.""".format(x, x, x-1))

    print("""1 bottle of beer on the wall, 1 bottle of beer.
    Take one down, pass it around, 1 bottle of beer on the wall""")

    return


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("""Age     Salary
    -----------------
    {}      {:,.2f}""".format(age, salary))
    for x in range(age, RETIREMENT):
        salary *= ((increase/100)+1)
        age += 1
        print("{}      {:,.2f}".format(age, salary))
    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    first_value = float(input("First value: "))
    total = first_value
    average = first_value
    maxum = first_value
    minum = first_value
    for x in range(1, n, 1):
        next_value = float(input("Next value: "))
        total += next_value
        if maxum < next_value:
            maxum = next_value
        if minum > next_value:
            minum = next_value
    average = total/n

    return minum, maxum, total, average,
