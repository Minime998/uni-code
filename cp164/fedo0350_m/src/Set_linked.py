"""
---------------------------------------
Set_linked.py
Linked version of the Set ADT
---------------------------------------
"""

from copy import deepcopy


class _Set_Node:

    def __init__(self, value, next_):
        """
        inits a set node
        """
        self._value = deepcopy(value)
        self._next = next_


class Set:

    def __init__(self):
        """
        inits an empty Set
        """
        self._front = None
        self._count = 0

    def is_empty(self):
        """
        determines if source is empty
        """
        return self._count == 0

    def __len__(self):
        """
        gets length
        """
        return self._count

    def _linear_search(self, key):
        """
        searches for the first occurrence of key in self
        """
        previous = None
        current = self._front

        while current is not None and current._value != key:
            previous = current
            current = current._next

        return previous, current

    def add(self, value):
        """
        adds value to end of source allows only one copy
        """
        new_node = _Set_Node(deepcopy(value), None)
        current = self._front

        if current is None:
            self._front = new_node
            inserted = True
            self._count += 1

        else:
            while current._next is not None and current._value != value:
                current = current._next

            if current._next is None:
                current._next = new_node
                inserted = True
                self._count += 1

            else:
                inserted = False

        return inserted

    def remove(self, key):
        """
        finds, removes, and returns the value from source
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
        remove from the front
        """
        if self._front is not None:
            value = self._front._value
            self._front = self._front._next
            self._count -= 1
        return value

    def find(self, key):
        """
        find and return copy of key
        """
        value = None
        _, current = self._linear_search(key)
        if current is not None:
            value = current._value

        return value

    def __contains__(self, key):
        _, current = self._linear_search(key)

        return current is not None

    def max(self):
        start_value = self._front._value
        current = self._front._next
        while current is not None:
            if start_value < current._value:
                start_value = current._value
            current = current._next
        return start_value

    def min(self):
        start_value = self._front._value
        current = self._front._next
        while current is not None:
            if start_value > current._value:
                start_value = current._value
            current = current._next
        return start_value

    def split_th(self):
        target1 = Set()
        target2 = Set()
        current = self._front
        count = 0

        if self._count > 0:
            while current is not None:
                if count <= (self._count // 2):
                    target1.add(current._value)
                    next = current._next
                    current = None
                    current = next
                    self._count -= 1
                    target1._count += 1
                    count += 1
                elif count >= (self._count // 2):
                    target2.add(current._value)
                    next = current._next
                    current = None
                    current = next
                    self._count -= 1
                    target2._count += 1
                    count += 1

        return target1, target2

    def __iter__(self):
        """
        testing
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
