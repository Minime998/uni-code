"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2021-03-22"
-------------------------------------------------------
"""
# [import statements]
from enum import Enum

from Movie import Movie
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue
from Stack_array import Stack

# [constants]
OPERATORS = "+-*/"
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    count = 0
    while not source.is_empty() and count % 2 == 0:
        target1.push(source.pop())
        count += 1
        while not source.is_empty() and count % 2 != 0:
            target2.push(source.pop())
            count += 1

    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    holding = []
    while not source.is_empty():
        holding.append(source.pop())
    i = len(holding)
    while i != 0:
        source.push(holding.pop(0))
        i = i - 1
    return


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    calc_stack = Stack()
    string_list = string.split()
    count = 0
    for x in range(len(string_list)):
        if string_list[x].isdigit() and count != 1:
            calc_stack.push(int(string_list[x]))
            count += 1
        elif string_list[x] in OPERATORS:
            if string_list[x] == "+":
                operator = calc_stack.pop()
                num = int(operator) + int(string_list[x + 1])
                calc_stack.push(num)
            elif string_list[x] == "-":
                operator = calc_stack.pop()
                num = int(operator) - int(string_list[x + 1])
                calc_stack.push(num)
            elif string_list[x] == "*":
                operator = calc_stack.pop()
                num = int(operator) * int(string_list[x + 1])
                calc_stack.push(num)
            elif string_list[x] == "/":
                operator = calc_stack.pop()
                num = int(operator) / int(string_list[x + 1])
                calc_stack.push(num)
    answer = float(calc_stack.pop())

    return answer


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    values_out = []
    order_stack = Stack()
    count = -1
    for x in range(len(opstring)):
        if opstring[x] == "S":
            count += 1
            order_stack.push(values_in[count])
        if opstring[x] == "X":
            values_out.append(order_stack.pop())

    return values_out


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        "cannot use '{}' as the mirror character".format(m)
    mirror = MIRRORED.IS_MIRRORED
    stack = Stack()
    n = len(string)
    i = 0

    while mirror == MIRRORED.IS_MIRRORED and i < n and string[i] != m:
        if string[i] in valid_chars:
            stack.push(string[i])
            i += 1
        else:
            mirror = MIRRORED.INVALID_CHAR

    if mirror == MIRRORED.IS_MIRRORED:
        i += 1
        while mirror == MIRRORED.IS_MIRRORED and i < n and not stack.is_empty():
            c = stack.pop()

            if string[i] != c:
                mirror = MIRRORED.NOT_MIRRORED
            else:
                i += 1
        if not (stack.is_empty() and i == n):
            mirror = MIRRORED.TOO_MANY_LEFT
    return mirror


def queue_is_identical(source1, source2):
    """
    ----------------
    Determines whether two given queues are identical. Entries of
    source1 and source2 are compared and if all contents are identical
    and in the same order, returns True, otherwise returns False.
    Use: identical = queue_is_identical(source1, source2)
    ---------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        identical - True if source1 and source2 are identical, False otherwise.
            source1 and source2 are unchanged. (boolean)
    ---------------
    """
    identical = True
    if len(source1) == len(source2):
        len1 = len(source1)
        count = 0
        while count != len1:
            value1 = source1.remove()
            value2 = source2.remove()
            source1.insert(value1)
            source2.insert(value2)
            count += 1
            if value1 != value2:
                identical = False
    else:
        identical = False

    return identical


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    while source.is_empty() is False:
        value = source.remove()
        if value >= key:
            target2.insert(value)
        elif value < key:
            target1.insert(value)
    return target1, target2


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x - 1, y) + recurse(x, y - 1)
    return ans


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:
        ans = n
    else:
        ans = gcd(n, m % n)
    return ans


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    count = 0
    if s != "":
        if s[0].lower() in vowels:
            count = 1 + vowel_count(s[1:])
        else:
            count = vowel_count(s[1:])
    return count


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        ans = 1
    elif power > 0:
        if power == 1:
            ans = base
        else:
            ans = base * to_power(base, power - 1)
    elif power < 0:
        if power == -1:
            ans = 1 / base
        else:
            ans = 1 / base * to_power(base, power + 1)
    return ans


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(s) > 1:
        if not s.isalpha():
            palindrome = is_palindrome(s[1:])
        elif not s[-1].isalpha():
            palindrome = is_palindrome(s[:-1])
        elif s[1].lower() == s[-1].lower():
            palindrome = is_palindrome(s[1:-1])
        else:
            palindrome = False
    else:
        palindrome = True
    return palindrome


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    new_set = []
    if bag == []:
        new_set = []
    else:
        if bag[-1] not in bag[:-1]:
            new_set = bag_to_set(bag[:-1]) + [bag[-1]]
        else:
            new_set = bag_to_set(bag[:-1])
    return new_set


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    for x in values:
        print("{} {}{}".format(hash(x), hash(x) % slots, str(x)))

    return
