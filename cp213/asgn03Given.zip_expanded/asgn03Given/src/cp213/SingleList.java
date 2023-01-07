package cp213;
import java.util.ArrayList;

/**
 * A single linked list structure of <code>Node T</code> objects. These data
 * objects must be Comparable - i.e. they must provide the compareTo method.
 * Only the <code>T</code> value contained in the priority queue is visible
 * through the standard priority queue methods. Extends the
 * <code>SingleLink</code> class.
 *
 * @author David Brown
 * @version 2021-09-24
 * @param <T> this SingleList data type.
 */
public class SingleList<T extends Comparable<T>> extends SingleLink<T> {

    /**
     * Searches for the first occurrence of key in this SingleList. Private helper
     * methods - used only by other ADT methods.
     *
     * @param key The value to look for.
     * @return A pointer to the node previous to the node containing key.
     */
    private SingleNode<T> linearSearch(final T key) {

	SingleNode<T> previous = null;
	SingleNode<T> current = this.front;
	
	while (current != null && current.getData().compareTo(key) != 0)
	{
		previous = current;
		current = current.getNext();
	}

	return previous;
    }

    /**
     * Appends data to the end of this SingleList.
     *
     * @param data The value to append.
     */
    public void append(final T data) {

	SingleNode<T> node = new SingleNode<T>(data, null);
	if (this.front == null)
	{
		this.front = node;
		this.rear = node;
	}
	else
	{
		this.rear.setNext(node);
		this.rear = node;
	}

	return;
    }

    /**
     * Removes duplicates from this SingleList. The list contains one and only one
     * of each value formerly present in this SingleList. The first occurrence of
     * each value is preserved.
     */
    public void clean() {

	SingleNode<T> previous = null;
	SingleNode<T> current = this.front;
	ArrayList<T> newlist1 = new ArrayList<T>();
	
	while (current != null)
	{
		for (T data: this)
		{
			if(!newlist1.contains(data))
			{
				newlist1.add(data);
				previous = current;
			}
			else
			{
				previous.setNext(current.getNext());
				this.length--;
			}
		}
		current = current.getNext();
	}

	return;
    }

    /**
     * Combines contents of two lists into a third. Values are alternated from the
     * origin lists into this SingleList. The origin lists are empty when finished.
     * NOTE: data must not be moved, only nodes.
     *
     * @param left  The first list to combine with this SingleList.
     * @param right The second list to combine with this SingleList.
     */
    public void combine(final SingleList<T> left, final SingleList<T> right) {

	while(left.length != 0 && right.length != 0)
	{
		this.moveFrontToRear(left);
		this.moveFrontToRear(right);
	}
	while(left.length != 0)
	{
		this.moveFrontToRear(left);
	}
	while(right.length != 0)
	{
		this.moveFrontToRear(right);
	}

	return;
    }

    /**
     * Determines if this SingleList contains key.
     *
     * @param key The key value to look for.
     * @return true if key is in this SingleList, false otherwise.
     */
    public boolean contains(final T key) {

	boolean isvalid = false;
	SingleNode<T> current = this.front;
	
	while(current != null)
	{
		if(current.getData().compareTo(key) == 0)
		{
			isvalid = true;
		}
		current = current.getNext();
	}

	return isvalid;
    }

    /**
     * Finds the number of times key appears in list.
     *
     * @param key The value to look for.
     * @return The number of times key appears in this SingleList.
     */
    public int count(final T key) {

	int counter = 0;
	SingleNode<T> current = this.front;
	
	while(current != null)
	{
		if(current.getData().compareTo(key)==0)
		{
			counter++;
		}
		current = current.getNext();
	}

	return counter;
    }

    /**
     * Finds and returns the value in list that matches key.
     *
     * @param key The value to search for.
     * @return The value that matches key, null otherwise.
     */
    public T find(final T key) {

	T number = null;
	if(this.length > 0)
	{
		SingleNode<T> previous = this.linearSearch(key);
		
		if(previous.getNext() != null)
		{
			number = previous.getNext().getData();
		}
	}
	
	

	return number;
    }

    /**
     * Get the nth item in this SingleList.
     *
     * @param n The index of the item to return.
     * @return The nth item in this SingleList.
     * @throws ArrayIndexOutOfBoundsException if n is not a valid index.
     */
    public T get(final int n) throws ArrayIndexOutOfBoundsException {

	T data = null;
	SingleNode<T> current = this.front;
	int counter = 0;
	
	while(current != null) {
		if (counter == n)
		{
			data = current.getData();
			break;
		}
		current = current.getNext();
		counter++;
	}

	return data;
    }

    /**
     * Determines whether two lists are identical.
     *
     * @param source The list to compare against this SingleList.
     * @return true if this SingleList contains the same values in the same order as
     *         source, false otherwise.
     */
    public boolean identical(final SingleList<T> source) {

	boolean identical;
	if(this.length != source.length)
	{
		identical = false;
	}
	else
	{
		SingleNode<T> sourceNode = this.front;
		SingleNode<T> targetNode = source.front;
		
		while(sourceNode != null &&(targetNode.getData()==sourceNode.getData()))
		{
			sourceNode = sourceNode.getNext();
			targetNode = targetNode.getNext();
		}
		identical = (sourceNode == null);
	}

	return identical;
    }

    /**
     * Finds the first location of a value by key in this SingleList.
     *
     * @param key The value to search for.
     * @return The index of key in this SingleList, -1 otherwise.
     */
    public int index(final T key) {

	int num = 0;
	SingleNode<T> current = this.front;
	
	while(current != null && current.getData() != key)
	{
		current = current.getNext();
		num++;
	}
	if(current == null)
	{
		num = -1;
	}

	return num;
    }

    /**
     * Inserts value into this SingleList at index i. If i greater than the length
     * of this SingleList, append data to the end of this SingleList.
     *
     * @param i     The index to insert the new data at.
     * @param data The new value to insert into this SingleList.
     */
    public void insert(int i, final T data) {

	int datainsert;
	
	if(i > this.length)
	{
		this.append(data);
	}
	else if((i < -this.length) || i ==0)
	{
		this.prepend(data);
	}
	else {
		if(i > 0)
		{
			datainsert = i;
		}
		else
		{
			datainsert = this.length + i;
		}
		int counter = 0;
		SingleNode<T> current = this.front;
		SingleNode<T> previous = null;
		while(counter < datainsert)
		{
			previous = current;
			current = current.getNext();
			counter++;
		}
		SingleNode<T> newnode = new SingleNode<T>(data,current);
		previous.setNext(newnode);
	}
this.length++;
	return;
    }

    /**
     * Creates an intersection of two other SingleLists into this SingleList. Copies
     * data to this SingleList. left and right SingleLists are unchanged. Values
     * from left are copied in order first, then values from right are copied in
     * order.
     *
     * @param left  The first SingleList to create an intersection from.
     * @param right The second SingleList to create an intersection from.
     */
    public void intersection(final SingleList<T> left, final SingleList<T> right) {

	SingleNode<T> current = left.front;
	
	while(current != null)
	{
		T data = current.getData();
		if(right.contains(data))
		{
			this.append(data);
		}
		current = current.getNext();
	}

	return;
    }

    /**
     * Finds the maximum value in this SingleList.
     *
     * @return The maximum value.
     */
    public T max() {

	SingleNode<T> current = this.front;
	T data = current.getData();
	
	while(current != null)
	{
		if(current.getData().compareTo(data) > 0)
		{
			data = current.getData();
		}
		current = current.getNext();
	}

	return data;
    }

    /**
     * Finds the minimum value in this SingleList.
     *
     * @return The minimum value.
     */
    public T min() {

	SingleNode<T> current = this.front;
	T mindata = current.getData();
	
	while(current != null)
	{
		if(current.getData().compareTo(mindata) < 0)
		{
			mindata = current.getData();
		}
		current = current.getNext();
	}

	return mindata;
    }

    /**
     * Inserts value into the front of this SingleList.
     *
     * @param data The value to insert into the front of this SingleList.
     */
    public void prepend(final T data) {

	if(this.front == null)
	{
		SingleNode<T> newdata = new SingleNode<T>(data,null);
		this.front = newdata;
		this.rear = newdata;
	}
	else
	{
		SingleNode<T> newdata = new SingleNode<T>(data,this.front);
		this.front = newdata;
	}
	this.length++;

	return;
    }

    /**
     * Finds, removes, and returns the value in this SingleList that matches key.
     *
     * @param key The value to search for.
     * @return The value matching key, null otherwise.
     */
    public T remove(final T key) {

        T data;
        SingleNode<T> previous = this.linearSearch(key);
        SingleNode<T> current = previous.getNext();
            
        if (current == null){
            data = null;
        }
        else{
            data = current.getData();
            if(previous.getData() == null) {
            	this.front = current.getNext();
            	if (current.getNext() == null) {
            		this.rear = current.getNext();
            	}
            }
            else {
            	previous.setNext(current.getNext());
            	if (current.getNext() == null) {
            		this.rear = previous;
            		}

            	}
            	
            }

	return data;
    }

    /**
     * Removes the value at the front of this SingleList.
     *
     * @return The value at the front of this SingleList.
     */
    public T removeFront() {

	T data = this.front.getData();
	this.front = this.front.getNext();
	this.length -= 1;

	return data;
    }

    /**
     * Finds and removes all values in this SingleList that match key.
     *
     * @param key The value to search for.
     */
    public void removeMany(final T key) {

    	SingleNode<T> previous = null;
        SingleNode<T> current = this.front;
        	
        while(current !=null) {
        	if (this.front.getData() == key) {
        		 front = front.getNext();
        		 if (this.length == 1) 
        			 rear = null;
        		 else 
        			 this.front = current.getNext();
        		 this.length--;
        	} else if (current.getData() == key) {
        		previous.setNext(current.getNext());
        		if (previous.getNext() == null)
        			this.rear = previous;
        		this.length--;
        		 
        	}
        	previous = current;
        	current = current.getNext();
        }

	return;
    }

    /**
     * Reverses the order of the values in this SingleList.
     */
    public void reverse() {

        SingleNode<T> frontdata = null;
        SingleNode<T> num = null;

        while (this.front != null) {
        	num = this.front.getNext();
        	this.front.setNext(frontdata);
        	frontdata = this.front;
        	this.front = num;
        }
        this.front = frontdata;

	return;
    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists.
     * Moves nodes only - does not move value or call the high-level methods insert
     * or remove. this SingleList is empty when done. The first half of this
     * SingleList is moved to left, and the last half of this SingleList is moved to
     * right. If the resulting lengths are not the same, left should have one more
     * item than right. Order is preserved.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void split(final SingleList<T> left, final SingleList<T> right) {

        int count = 0;
        int val = this.getLength();
       	int num = Math.floorDiv(val, 2);
        	
        if (val % 2 == 0) {
            while (count != num) {
                left.moveFrontToRear(this);
               	count++;
            }
            while(count != val) {
                right.moveFrontToRear(this);
                count++;
            }
        }
        else {
            while (count != (num+1)) {
                left.moveFrontToRear(this);
               	count++;
            }
            count++;
            while (count != (length+1)) {
                right.moveFrontToRear(this);
               	count++;
            }
        }

	return;
    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists.
     * Moves nodes only - does not move value or call the high-level methods insert
     * or remove. this SingleList is empty when done. Nodes are moved alternately
     * from this SingleList to left and right. Order is preserved.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void splitAlternate(final SingleList<T> left, final SingleList<T> right) {

        boolean check = true;
    	
        while (this.front != null) {
        	if (check == true) {
        		left.moveFrontToRear(this);
        		check = false;
        	}
        	else {
        		right.moveFrontToRear(this);
        		check = true;
        	}
        }

	return;
    }

    /**
     * Creates a union of two other SingleLists into this SingleList. Copies value
     * to this list. left and right SingleLists are unchanged. Values from left are
     * copied in order first, then values from right are copied in order.
     *
     * @param left  The first SingleList to create a union from.
     * @param right The second SingleList to create a union from.
     */
    public void union(final SingleList<T> left, final SingleList<T> right) {

        SingleNode<T> node1 = left.front;
        SingleNode<T> node2 = right.front;
            
        while (node1 != null) {
            T value = node1.getData(); 
            this.append(value);
            node1 = node1.getNext();
            
       }     
       while (node2 != null) {
            T value = node2.getData(); 
            if (!this.contains(value)) {
               this.append(value);
            }
           node2 = node2.getNext();
       }

	return;
    }
}
