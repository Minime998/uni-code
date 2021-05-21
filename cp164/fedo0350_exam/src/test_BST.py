"""
-------------------------------------------------------
Simple BST testing - Exam
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2021-04-18"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
SEP = '-' * 60
values = [11, 7, 6, 9, 8, 15, 12]

print("Test _rotate_right")
print()
print("Create a BST with {}".format(values))
bst = BST()

for v in values:
    bst.insert(v)

a = bst.preorder()
print("  Preorder: {}".format(a))
print("Rotate the tree around the root node (11)")
bst._root = bst._rotate_right(bst._root)
a = bst.preorder()
print("  Preorder: {}".format(a))
print()
print(SEP)
print("Test mirror")
print()
print("Create a BST with {}".format(values))
bst = BST()

for v in values:
    bst.insert(v)

a = bst.preorder()
print("  Preorder: {}".format(a))
a = bst.inorder()
print("  Inorder: {}".format(a))
print("Mirror the tree")
bst.mirror()
a = bst.preorder()
print("  Preorder: {}".format(a))
a = bst.inorder()
print("  Inorder: {}".format(a))
