"""
-------------------------------------------------------
Simple Radix string sort testing - Exam
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2021-04-18"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts
from string import ascii_lowercase
from random import shuffle

# Constants
ALPHABET = "abcde"
SEP = '-' * 60

# Testing
print("Test Radix String Sort")
print()
print(SEP)
print()
print("Test single lower case letters")
# Generate a random list of lower case alphabet characters
strings = list(ascii_lowercase)
shuffle(strings)
print(strings)
Sorts.radix_string_sort(strings)
print("Sorted: {}".format(Sorts.is_sorted(strings)))
print(strings)
print()
print(SEP)
print()
print("Test lower case words")
strings = ["david", "tasmin", "tristan", "deborah", "lori",
           "zephyr", "wolverine", "ptarmigan", "whatever", "aardvark"]
shuffle(strings)
print(strings)
Sorts.radix_string_sort(strings)
print("Sorted: {}".format(Sorts.is_sorted(strings)))
print(strings)
print()
print(SEP)
print()
print("Test mixed case words")
strings = ["David", "Tasmin", "Tristan", "Deborah", "Lori",
           "zephyr", "wolverine", "ptarmigan", "whatever", "aardvark"]
shuffle(strings)
print(strings)
Sorts.radix_string_sort(strings)
print("Sorted: {}".format(Sorts.is_sorted(strings)))
print(strings)
