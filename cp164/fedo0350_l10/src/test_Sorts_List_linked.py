"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2021-03-29"
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for x in range(0, SIZE):
        values.append(Number(x))
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()

    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = List()
    for x in range(TESTS):
        lists.append([])
    for lis in lists:
        for x in range(SIZE):
            lis.append(Number(random.randint(0, XRANGE)))

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    sorted_list = create_sorted()
    rev_list = create_reversed()
    random_list = create_randoms()

    func(sorted_list)
    sorted_compare = Number.comparisons
    sorted_swaps = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0
    func(rev_list)
    rev_compare = Number.comparisons
    rev_swaps = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0
    func(random_list)
    rand_compare = Number.comparisons
    rand_swaps = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0

    print(title, "comparisons:", sorted_compare, rev_compare, rand_compare,)
    print(title, "swaps:", sorted_swaps, rev_swaps, rand_swaps,)

    return
