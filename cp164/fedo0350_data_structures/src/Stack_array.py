'''
Stacks

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-02-04"

'''

from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an is_empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the stack is empty, False otherwise
        -------------------------------------------------------
        """

        return len(self._values) == 0

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"
        value = deepcopy(self._values.pop(-1))
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"
        value = deepcopy(self._values[-1])
        return value

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        count = 0
        while len(self._values) != 0 and count % 2 == 0:
            target1._values.append(self._values.pop())
            count += 1
            while len(self._values) != 0 and count % 2 != 0:
                target2._values.append(self._values.pop())
                count += 1

        return target1, target2

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        holding = []
        while not len(self._values) == 0:  # why use not?
            holding.append(self._values.pop())
        i = len(holding)
        for x in range(i):
            self._values.append(holding[x])
        return

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
