"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-19"
-------------------------------------------------------
"""
# [import statements]

# [constants]


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:10]

    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:8]
    end = product_code[7:]

    if pc.isalpha() and pc.isupper() and len(pc) == 3:
        print("Category {} is valid.".format(pc))
    else:
        print("Category {} is not valid.".format(pc))
    if pi.isdigit() and len(pi) == 4:
        print("ID {} is valid.".format(pi))
    else:
        print("ID {} is not valid.".format(pi))
    if len(pq) == 1 and pq.isupper():
        print("Qualifier {} is valid.".format(end))
    else:
        print("Qualifier {} is not valid.".format(end))

    return


def digit_count(s):
    """
    -------------------------------------------------------
    Counts the number of digits in a string.
    Use: count = digit_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of digits in s (int)
    -------------------------------------------------------
    """
    count = 0
    length = len(s)
    for i in range(length):
        if s[i].isdigit():
            count += 1
    return count


def total_digits(s):
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
    length = len(s)
    for i in range(length):
        if s[i].isdigit():
            total += int(s[i])
    return total


def calculate(expr):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """
    result = 0
    middle = expr[2:3]
    first = expr[0]
    last = expr[4]
    if middle == "+":
        result += int(first) + int(last)
    elif middle == "%":
        if last == "0":
            result = None
        else:
            result += int(first) % int(last)
    elif middle == "-":
        result += int(first) - int(last)
    elif middle == "*":
        result += int(first) * int(last)
    elif middle == "/":
        if last == "0":
            result = None
        else:
            result += int(first) / int(last)

    return result
