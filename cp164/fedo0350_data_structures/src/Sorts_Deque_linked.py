"""
-------------------------------------------------------
Linked versions of various sorts. Implemented on linked Deques.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2021-04-07"
-------------------------------------------------------
"""
from math import log
from Deque_linked import Deque


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times 
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def gnome_sort(a):
        """
        -------------------------------------------------------
        Sorts a Deque using the Gnome Sort algorithm.
        Use: gnome_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked structure of comparable elements (Deque)
        Returns:
            None
        -------------------------------------------------------
        """
        current = a._front

        while current is not None:
            if current._prev is None:
                current = current._next

            if current._value >= current._prev._value:
                current = current._next

            else:
                temp = current._prev._value  # copy swap
                temp_two = current._value
                current._value = temp
                current._prev._value = temp_two
                current = current._prev
        return

    # Sort Utilities

    @staticmethod
    def sort_test(a):
        """
        -------------------------------------------------------
        Determines whether a linked deque is sorted or not.
        Use: sort_test(a)
        -------------------------------------------------------
        Parameters:
            a - a linked deque of comparable elements (?)
        Returns:
            returns
            is_sorted - True if contents of a are sorted, False otherwise.
        -------------------------------------------------------
        """
        is_sorted = True
        # Test forward links
        current = a._front

        while is_sorted and current is not None and \
                current._next is not None:

            if current._value <= current._next._value:
                current = current._next
            else:
                is_sorted = False
        # Test reverse links
        current = a._rear

        while is_sorted and current is not None and \
                current._prev is not None:

            if current._value >= current._prev._value:
                current = current._prev
            else:
                is_sorted = False

        return is_sorted
