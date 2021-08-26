'''
[program description]

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-03-25"

'''

from Letter import Letter

# Constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains 
    the number of comparisons found by searching for that Letter 
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects 
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    file_variable.seek(0)

    for line in file_variable:

        for char in line.strip():

            if char.isalpha():
                l = Letter(char.upper())
                bst.retrieve(l)
    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    bst_inorder = bst.inorder()

    for x in bst_inorder:
        total = total + x.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    counter = 0
    bst_inorder = bst.inorder()

    for x in bst_inorder:
        counter += x.count
    print("Letter Count/Percent Table")
    print()
    print("Total Count: {:,}".format(counter))
    print()
    print("Letter  Count          %")
    print("------------------------")
    for x in bst_inorder:
        print("{:>2}{:9,d}{:>13.2%}".format(
            x.letter, x.count, x.count / counter))
    return
