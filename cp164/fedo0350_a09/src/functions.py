'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-04-01"

'''
from Word import Word


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in fv and inserts into
    a Hash_Set.
    Each Word object in hash_set contains the number of comparisons
    required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    lines = fv.readline()

    for lines in fv:
        for word in lines.strip().split(" "):
            if word.isalpha():
                hash_set.insert(Word(word.lower()))

        lines = fv.readline()
    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = None
    for x in hash_set:
        total += x.comparisons
        if max_word is None:
            max_word = x
        elif x.comparisons > max_word.comparisons:
            max_word = x

    return total, max_word
