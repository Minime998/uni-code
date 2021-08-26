"""
-------------------------------------------------------
Linked version of the Set ADT - Exam
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
Section: CP164 B
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Set_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a Set node that contains a copy of value
        and a link to another Set node.
        Use: node = _Set_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Set node (_Set_Node)
        Returns​‌​‌​‌​​:
            a new _Set_Node object (_Set_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Set.
        Use: target = Set()
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if Set is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns​‌​‌​‌​​:
            True if Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in Set.
        Use: n = len(source)
        -------------------------------------------------------
        Returns​‌​‌​‌​​:
            the number of values in Set.
        -------------------------------------------------------
        """
        return self._count

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for key in Set.
        (Private helper method)
        Use: prev, curr = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​‌​‌​‌​​:
            prev - pointer to node prev to the node containing key (_Set_Node)
            curr - pointer to node containing key, None if not found (_Set_Node)
        -------------------------------------------------------
        """
        previous = None
        current = self._front

        while current is not None and current._value != key:
            previous = current
            current = current._next

        return previous, current

    def add(self, value):
        """
        -------------------------------------------------------
        Adds value to end of Set. Values may appear only once in the Set.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns​‌​‌​‌​​:
            added - True if value is added to Set, False otherwise (boolean)
        -------------------------------------------------------
        """
        new_node = _Set_Node(deepcopy(value), None)
        current = self._front

        if current is None:
            self._front = new_node
            added = True
            self._count += 1
        else:
            while current._next is not None and current._value != value:
                current = current._next

            if current._next is None:
                current._next = new_node
                added = True
                self._count += 1
            else:
                added = False

        return added

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns value in Set that matches key.
        Returns None if no matching value.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​‌​‌​‌​​:
            value - the value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current = self._linear_search(key)
        if current is None:
            value = None
        else:
            value = current._value
            self._count -= 1
            if previous is None:
                self._front = self._front._next
            else:
                previous._next = current._next
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns first value in Set.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns​‌​‌​‌​​:
            value - first value in Set (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty set"
        if self._front is not None:
            value = self._front._value
            self._front = self._front._next
            self._count -= 1
        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Returns a copy of value in Set that matches key, None
        if key is not found.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​‌​‌​‌​​:
            value - a copy of value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        _, current = self._linear_search(key)
        if current is not None:
            value = current._value

        return value

    def __contains__(self, key):
        """
        -------------------------------------------------------
        Determines if Set contains a value matching key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​‌​‌​‌​​:
            True if Set contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        _, current = self._linear_search(key)

        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Returns a copy of maximum value in Set.
        Use: value = source.max()
        -------------------------------------------------------
        Returns​‌​‌​‌​​:
            value - a copy of maximum value in Set (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot find maximum of an empty set"
        start_value = self._front._value
        current = self._front._next
        while current is not None:
            if start_value < current._value:
                start_value = current._value
            current = current._next
        return start_value

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from source to self and updates the
        count of both. Does not check to see if moved front node
        is unique in self. Moves nodes, not data, between Sets.
        (Private helper method)
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked Set (Set)
        Returns​‌​‌​‌​​:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty Set"
        if source._front is None:
            self._front = source._front
            self._count += 1
            if source._front._next is not None:
                source._front = source._front._next
            source._count -= 1
        else:
            source._front._next = self._front
            self._front = source._front
            self._count += 1
            source._front = source._front._next
            source._count -= 1
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits source Set into separate target Sets with values
        alternating in the targets. At finish source Set is empty.
        Order of values in target Sets is irrelevant. Moves nodes,
        not data, between Sets.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns​‌​‌​‌​​:
            target1 - contains alternating values from source (Set)
            target2 - contains other alternating values from source (Set)
        -------------------------------------------------------
        Examples:
            (1) splits into (1), ()
            (1,2,3,6,9,11,8) splits into (8,9,3,1), (11,6,2)
        -------------------------------------------------------
        """
        iterbool = True
        target1 = Set()
        target2 = Set()

        while self._front is not None:
            if iterbool:
                target1._move_front_to_front(self)
            else:
                target2._move_front_to_front(self)

            iterbool = not iterbool

        return target1, target2

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source Sets into target. When finished, contents of
        source1 and source2 are interlaced into target and source1 and source2
        are empty. Values may appear only once in target. Order of values in
        target Set is irrelevant. Moves nodes, not data, between Sets.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked set (Set)
            source2 - a linked set (Set)
        Returns​‌​‌​‌​​:
            None
        -------------------------------------------------------
        Examples:
            (1,2,3) combine () is (3,2,1)
            () combine (1,2,3) is (3,2,1)
            (1,2,3) combine (3,2,1) is (3,2,1)
            (1,2,3) combine (3,4,5) is (5,4,2,3,1)
        -------------------------------------------------------
        """
        iterbool = True
        target = Set()

        if source1._count >= source2._count:  # check for bigger one
            thing1 = source1._front
            thing2 = source2._front
        else:
            thing1 = source2._front
            thing2 = source1._front
        while thing1 is not None:
            if iterbool:
                target._move_front_to_front(source1)
            elif thing2 is not None:
                target._move_front_to_front(source2)

            iterbool = not iterbool

        return

    def isdisjoint(self, source):
        """
        -------------------------------------------------------
        Determines if self is disjoint with source. self is disjoint
        with source if self and source have no values in common.
        Use: disjoint = self.isdisjoint(source)
        -------------------------------------------------------
        Parameters:
            source - a set (Set)
        Returns​‌​‌​‌​​:
            disjoint - True if self and source have no values in common,
                otherwise False (boolean)
        -------------------------------------------------------
        Examples:
            () isdisjoint (3,2,1) is True
            (1,2,3) isdisjoint (3,2,1) is False
            (1,2,3) isdisjoint (4,5,6) is True
            (2,4,6) isdisjoint (0,2,4,8) is False
        -------------------------------------------------------
        """
        current = self._front
        currentother = source._front
        disjoint = True

        while current is not None and disjoint is True:
            while source is not None and disjoint is True:
                if current._value == currentother._value:
                    disjoint = False
                else:
                    currentother = currentother._next

            currentother = source._front
            current = current._next

        return disjoint

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the set
        from first to last items.
        Use: for v in set:
        -------------------------------------------------------
        Returns​‌​‌​‌​​:
            yields
            value - the next value in the set (?)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next
