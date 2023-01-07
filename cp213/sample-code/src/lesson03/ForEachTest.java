package lesson03;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class ForEachTest {

	public static void main(String args[]) {
//		double sum = 0;
//		double[] price = { 1.5, 2.5, 3.5, 4, 0.5 };
//
////basic for loop
//		for (int i = 0; i < price.length; i++) {
//			sum = sum + price[i];
//		}
//		System.out.println(sum);
//
////for-each loop is used  
//		sum = 0;
//		for (double p : price)
//			sum = sum + p;
//		System.out.println(sum);
//		
//		
//		
		
		Collection<String> myCollectionItem = new ArrayList<String> () ;
        myCollectionItem.add("1 - H - Hydrogen")  ; 
        myCollectionItem.add("2 - He - Helium")  ; 
        myCollectionItem.add("3 - Li - Lithium")  ; 
        myCollectionItem.add("4 - Be - Beryllium")  ; 
        myCollectionItem.add("5 - B - Boron")  ; 
        
        Iterator iter = myCollectionItem.iterator() ; 
        while (iter.hasNext()) {
                        System.out.println(iter.next())  ; 
        }              
        // Or using for-each :  
        System.out.println ("for-each is used:") ; 
        for (String item: myCollectionItem)
                        System.out.println (item) ;

	}
}
