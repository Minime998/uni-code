"""
-------------------------------------------------------
Set_array.py
Array version of the Set ADT.
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2021-03-03"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy

"""
The PyDev module 'test_Set.py' contains a few sample tests for some of the Set
methods. The method 'print_set' is a testing method that shows you the complete
contents of a Set object in human-readable form and can also be used for testing.
"""


class Set:
    """
    -------------------------------------------------------
    Data structure that contains a set of unique values,
        i.e. no values are repeated in a Set.
    Values stored in fixed-length Python list like in the Circular Queue.
        Do not use Python list methods that change the length of the list:
            append, insert, remove, pop, extend, delete
    Empty slots contain None.
    -------------------------------------------------------
    Examples of Set attributes:
        _values = [None, None, None, None], _max_size = 4, _count = 0, _slot = 0
        _values = [1, None, 9, None],       _max_size = 4, _count = 2, _slot = 1
        _values = [1, None, 9, 3],          _max_size = 4, _count = 3, _slot = 1
        _values = [1, 4, None, 3],          _max_size = 4, _count = 3, _slot = 2
        _values = [1, 4, 9, 3],             _max_size = 4, _count = 4, _slot = None
    -------------------------------------------------------
    """
    # Default maximum size when max_size parameter is not provided
    DEFAULT_SIZE = 10

    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Efficiency: O(1)
        -------------------------------------------------------
        Initializes an empty Set.
        Use: target = Set(max_size)
        Use: target = Set()  # uses DEFAULT_SIZE
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the set (int > 0)
        Returns​​‌​‌​‌​‌:
            a new Set object (Set)
        -------------------------------------------------------
        """
        # Maximum size of Python list to store data.
        self._max_size = max_size
        # Python list that stores data - initialized to list of None.
        self._values = [None] * self._max_size
        # First available index for adding values -set to None if Set is full.
        self._slot = 0
        # Number of unique values in Set. Cannot exceed _max_size.
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Efficiency: O(1)
        -------------------------------------------------------
        Determines if the set is empty. In an empty set, all slots
        in _values contain None.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns​​‌​‌​‌​‌:
            True if the set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count != 0

    def is_full(self):
        """
        -------------------------------------------------------
        Efficiency: O(1)
        -------------------------------------------------------
        Determines if the set is full. In a full set, no slot
        in _values is None.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns​​‌​‌​‌​‌:
            True if the set is full, False otherwise.
        -------------------------------------------------------
        """
        return self._count == self._max_size

    def __len__(self):
        """
        -------------------------------------------------------
        Efficiency: O(1)
        -------------------------------------------------------
        Returns the number of non-None values in the set.
        Use: n = len(source)
        -------------------------------------------------------
        Returns​​‌​‌​‌​‌:
            the number of values in the set.
        -------------------------------------------------------
        """
        return self._count

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Searches for the occurrence of key in the set. Skips over None entries.
        (Private helper method - used only by other ADT methods.)
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​​‌​‌​‌​‌:
            i - the index of key in the set, -1 if key is not found (int)
        -------------------------------------------------------
        """
        if self._count > 0:
            i = 0
            nums = len(self._values)
            while i < nums and self._values != key:
                i += 1
            if i == nums and self._values[nums - 1] != key:
                i = -1
        else:
            i = -1
                
        return i

    def _set_slot(self):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Sets the value of _slot, the index of the first location of None
        in _values.
        (Private helper method - used only by other ADT methods.)
        Use: self._set_slot()
        -------------------------------------------------------
        Returns​​‌​‌​‌​‌:
            None
        -------------------------------------------------------
        """
        count = 0
        for i in self._values:
            if i is None:
                self._slot = count
                return self._slot

            count += 1

    def insert(self, value):
        """
        -------------------------------------------------------
        Efficiency: O(n) 
        -------------------------------------------------------
        Adds value to the set at index _slot.
        Use: inserted = source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns​​‌​‌​‌​‌:
            inserted - True if value was added to source, False otherwise.
                value is added only if value is unique in the set (boolean)
        -------------------------------------------------------
        """
        assert self._slot is not None, "Cannot add to a full set"
        inserted = False 
        
        i = self._linear_search(value)
        self._set_slot() 
        if i == -1:
            self._values[self._slot] = value
            inserted = True
            self._count += 1
            self._set_slot()
            
        return inserted

    def delete(self, key):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Finds, removes, and returns the value in the set that matches key.
        Updates _slot.
        Use: value = source.delete(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​​‌​‌​‌​‌:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        count = 0
        value = None
        for i in self._values:
            if i == key:
                value = self._values.pop(count)
                self._count -= 1
                self._max_size -= 1

            count += 1

        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Finds and returns a copy of value in the set that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​​‌​‌​‌​‌:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        for i in self._values:
            if i == key:
                value = deepcopy(i)

        return value

    def __contains__(self, key):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        ---------------------------------------------------------
        Determines if the set contains a value matching key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​​‌​‌​‌​‌:
            True if the set contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        cont = False

        for i in self._values:
            if i == key:
                cont = True

        return cont

    def maximum(self):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Returns a copy of the maximum value in the set.
        Use: value = source.maximum()
        -------------------------------------------------------
        Returns​​‌​‌​‌​‌:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot find maximum of an empty set"
        value = self._values[0]

        for i in self._values:
            if i > value:
                value = deepcopy(i)

        return value

    def minimum(self):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Returns a copy of the minimum value in the set.
        Use: value = source.minimum()
        -------------------------------------------------------
        Returns​​‌​‌​‌​‌:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot find minimum of an empty set"
        value = self._values[0]

        for i in self._values:
            if i < value:
                value = deepcopy(i)

        return value

    def intersection(self, source):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Returns a new set with only the values that appear in both
        self and source.
        Maximum size of target Set is the smaller of the maximum sizes of
            self and source.
        Use: target = self.intersection(source)
        -------------------------------------------------------
        Parameters:
            source - a set (Set)
        Returns​​‌​‌​‌​‌:
            target - a set containing one copy of all the values
                that appear in both self and source (Set)
        -------------------------------------------------------
        Examples:
            (1,2,3) intersection (3,2,1) is (1,2,3)
            (1,2,3) intersection (4,5,6) is ()
            (1,2,3,4,5,6) intersection (0,2,4,6,8) is (2,4,6)
        -------------------------------------------------------
        """
        target = Set()
        for i in source._values:
            if i in self._values and i not in target:
                target.append(i)
        return target

    def difference(self, source):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Return a set that contains the items that only exist in
        self and not in source.
        Maximum size of target Set is the maximum size of self.
        Use: target = self.difference(source)
        -------------------------------------------------------
        Parameters:
            source - a set (Set)
        Returns​​‌​‌​‌​‌:
            target - a set containing one copy of all the values
                in self that are not in source (Set)
        -------------------------------------------------------
        Examples:
            (1,2,3) difference (3,2,1) is ()
            (1,2,3) difference (4,5,6) is (1,2,3)
            (1,2,3,4,5,6) difference (0,2,4,6,8) is (1,3,5)
        -------------------------------------------------------
        """

        # your code here

    def print_set(self):
        """
        -------------------------------------------------------
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Prints the contents of a Set in human readable format.
        Use: source.print_set()
        -------------------------------------------------------
        Returns​​‌​‌​‌​‌:
            None
        -------------------------------------------------------
        """
        print("_values:   {}".format(self._values))
        print("_max_size: {:2d}".format(self._max_size))
        print("_count:    {:2d}".format(self._count))
        print("_slot:     {:2d}".format(self._slot))
        print("----------")
        return

    def __iter__(self):
        """
        -------------------------------------------------------
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the set
        from left to right.
        Use: for v in source:
        -------------------------------------------------------
        Returns​​‌​‌​‌​‌:
            value - the next value in the set (?)
        -------------------------------------------------------
        """
        for value in self._values:
            if value is not None:
                yield value
