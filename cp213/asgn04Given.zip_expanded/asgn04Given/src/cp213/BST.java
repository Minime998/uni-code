package cp213;

import java.util.ArrayList;

/**
 * Implements a Binary Search Tree.
 *
 * @author your name here
 * @author David Brown
 * @version 2021-11-01
 */
public class BST<T extends Comparable<T>> {
    protected int comparisons = 0; // Count of comparisons performed by tree.

    // Attributes.
    protected TreeNode<T> root = null; // Root node of the tree.
    protected int size = 0; // Number of elements in the tree.

    /**
     * Auxiliary method for {@code equals}. Determines whether two subtrees are
     * identical in items and height.
     *
     * @param source Node of this BST.
     * @param target Node of that BST.
     * @return true if source and target are identical in items and height.
     */
    protected boolean equalsAux(final TreeNode<T> source, final TreeNode<T> target) {

    	boolean equalstatus = false;

		if (source == null && target == null) {
			equalstatus = true;

		} else if (source != null && target != null && source.getItem().compareTo(target.getItem()) == 0 && source.getHeight() == target.getHeight() && source.getItem().getCount() == target.getItem().getCount()) {
			equalstatus = this.equalsAux(source.getLeft(), target.getLeft()) && this.equalsAux(source.getRight(), target.getRight());
		} 
		
		else {
			equalstatus = false;
		}
		return equalstatus;
    }

    /**
     * Auxiliary method for {@code insert}. Inserts data into this BST.
     *
     * @param node the current node (TreeNode)
     * @param data data to be inserted into the node
     * @return the inserted node.
     */
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedItem<T> data) {
    	if (node == null) {
			data.incrementCount();
			node = new TreeNode<T>(data);
			this.size++;
		} else {
			final int result = node.getItem().compareTo(data);
			if (result > 0) {
				node.setLeft(this.insertAux(node.getLeft(), data));
			} else if (result < 0) {
				node.setRight(this.insertAux(node.getRight(), data));
			} else {
				this.size++;
			}
		}
		node.updateHeight();
		return node;
    }

    /**
     * Auxiliary method for {@code valid}. Determines if a subtree based on node is
     * a valid subtree.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {
    	boolean validstatus = false;

		if (node == null) {
			validstatus = true;
		} else if (Math.max(this.nodeHeight(node.getLeft()), this.nodeHeight(node.getRight())) != node.getHeight() - 1) {
			validstatus = false;
		} else if (node.getLeft() != null && node.getLeft().getItem().compareTo(node.getItem()) >= 0
				|| node.getRight() != null && node.getRight().getItem().compareTo(node.getItem()) <= 0) {
			validstatus = false;
		} else {
			validstatus = this.isValidAux(node.getLeft(), minNode, maxNode)
					&& this.isValidAux(node.getRight(), minNode, maxNode);
		}
		return validstatus;
    }

    /**
     * Returns the height of a given TreeNode.
     *
     * @param node The TreeNode to determine the height of.
     * @return The item of the height attribute of node, 0 if node is null.
     */
    protected int nodeHeight(final TreeNode<T> node) {
	int height = 0;

	if (node != null) {
	    height = node.getHeight();
	}
	return height;
    }

    /**
     * Determines if this BST contains key.
     *
     * @param key The key to search for.
     * @return true if this BST contains key, false otherwise.
     */
    public boolean contains(final CountedItem<T> key) {

    	boolean contstatus = this.retrieve(key) != null;

		return contstatus;
    }

    /**
     * Determines whether two BSTs are identical.
     *
     * @param target The BST to compare this BST against.
     * @return true if this BST and that BST contain nodes that match in position,
     *         item, count, and height, false otherwise.
     */
    public boolean equals(final BST<T> target) {
	boolean isEqual = false;

	if (this.size == target.size) {
	    isEqual = this.equalsAux(this.root, target.root);
	}
	return isEqual;
    }

    /**
     * Get number of comparisons executed by the {@code retrieve} method.
     *
     * @return comparisons
     */
    public int getComparisons() {
	return this.comparisons;
    }

    /**
     * Returns the height of the root node of this BST.
     *
     * @return height of root node, 0 if the root node is null.
     */
    public int getHeight() {
	int height = 0;

	if (this.root != null) {
	    height = this.root.getHeight();
	}
	return height;
    }

    /**
     * Returns the number of nodes in the BST.
     *
     * @return number of node in this BST.
     */
    public int getSize() {
	return this.size;
    }

    /**
     * Returns an array of copies of CountedItem objects in a linked data
     * structure. The array contents are in data order from smallest to largest.
     *
     * Not thread safe as it assumes contents of data structure are not changed by
     * an external thread during the copy loop. If data elements are added or
     * removed by an external thread while the data is being copied to the array,
     * then the declared array size may no longer be valid.
     *
     * @return this tree data as an array of data.
     */
    public ArrayList<CountedItem<T>> inOrder() {
	return this.root.inOrder();
    }

    /**
     * Inserts data into this BST.
     *
     * @param data Data to store.
     */
    public void insert(final CountedItem<T> data) {
    	if (this.isEmpty()) {
			this.root = new TreeNode<T>(data);
			this.size++;
			data.incrementCount();
		} else {
			this.root = this.insertAux(this.root, data);
		}
		return;
    }

    /**
     * Determines if this BST is empty.
     *
     * @return true if this BST is empty, false otherwise.
     */
    public boolean isEmpty() {
	return this.root == null;
    }

    /**
     * Determines if this BST is a valid BST; i.e. a node's left child data is
     * smaller than its data, and its right child data is greater than its data, and
     * a node's height is equal to the maximum of the heights of its two children
     * (empty child nodes have a height of 0), plus 1.
     *
     * @return true if this BST is a valid BST, false otherwise.
     */
    public boolean isValid() {
	return this.isValidAux(this.root, null, null);
    }

    /**
     * Returns an array of copies of CountedItem objects int a linked data
     * structure. The array contents are in level order starting from the root
     * (this) node. Helps determine the structure of the tree.
     *
     * Not thread safe as it assumes contents of data structure are not changed by
     * an external thread during the copy loop. If data elements are added or
     * removed by an external thread while the data is being copied to the array,
     * then the declared array size may no longer be valid.
     *
     * @return this tree data as an array of data.
     */
    public ArrayList<CountedItem<T>> levelOrder() {
	return this.root.levelOrder();
    }

    /**
     * Resets the comparison count to 0.
     */
    public void resetComparisons() {
	this.comparisons = 0;
	return;
    }

    /**
     * Retrieves a copy of data matching key (key should have item
     * count of 0). Returning a complete CountedItem gives access to the
     * item and count.
     *
     * @param key The key to look for.
     * @return data The complete CountedItem that matches key, null otherwise.
     */
    public CountedItem<T> retrieve(final CountedItem<T> key) {

		TreeNode<T> node = this.root;
		CountedItem<T> item = null;
		while (node != null && item == null) {
			
			final int result = node.getItem().compareTo(key);
			this.comparisons++;
			if (result > 0) {
				node = node.getLeft();
			} else if (result < 0) {
				node = node.getRight();
			} else {
				item = node.getItem();
			}
		}

		return item;
    }
}
