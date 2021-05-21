"""
-------------------------------------------------------
Array versions of various sorts - Exam
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
Section: CP164 B
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
import string


class Sorts:
    # The Sorts

    @staticmethod
    def radix_string_sort(strings):
        """
        -------------------------------------------------------
        Performs a string radix sort.
        Use: Sorts.radix_string_sort(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns​‌​‌​‌​​:
            None
        -------------------------------------------------------
        """
        temp_list = []
        for x in strings:
            temp_list.append(x)
        temp_num_list = []
        for x in temp_list:
            temp_num_list.append(ord(x))
        strings = []
        for x in temp_num_list:
            strings.append(x)
        print(strings)
        
        length = len(strings)
        max_element = max(strings)
        digits = len(str(max_element))
        radix_lists = []
        bucket = [radix_lists] * 10

        for x in range(digits):
            for length_num in range(length):
                sorting_num = int((strings[length_num] / pow(10, x)) % 10)
                if len(bucket[sorting_num]) > 0:
                    bucket[sorting_num].append(strings[length_num])
                else:
                    bucket[sorting_num] = [strings[length_num]]
            counter = 0
            for y in range(10):
                if len(bucket[y]) > 0:
                    for _ in range(len(bucket[y])):
                        strings[counter] = bucket[y].pop(0)
                        counter += 1
        temp_letter_list = []
        for x in strings:
            temp_letter_list.append(chr(x))
        print(temp_letter_list)
        strings = temp_letter_list
        return

    @staticmethod
    def is_sorted(a):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: b = Sorts.is_sorted(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns​‌​‌​‌​​:
            srtd - True if contents of a are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        n = len(a)
        i = 0

        while srtd and i < n - 1:

            if a[i].lower() <= a[i + 1].lower():
                i += 1
            else:
                srtd = False
        return srtd
