"""
-------------------------------------------------------
Tests various array-based sorting functions.
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
from Number import Number
from Sorts_array import Sorts

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
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []

    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []

    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))

    # your code here

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TEST rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    arrays = []
    for x in range(TESTS):
        arrays.append([])
    for lists in arrays:
        for x in range(SIZE):
            lists.append(Number(random.randint(0, XRANGE)))
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
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
