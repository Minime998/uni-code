package lesson03;

import java.util.Scanner;



public class SwitchClass {
	
	public static void innerBreak () {
		
		boolean notFound = false ; 
		
	    for (int i = 0; i < 10 && !notFound; i++) {
	    	
	        for ( int j = 0; j < 10 &&  !notFound ;  j++) {
	        	
	            System.out.println (" inner loop") ; 
	            notFound = true ; 
	           }
	        
	       System.out.println (" out loop") ; 
	      }
	}


	
	
	public static void labeledBreak () {
		
		boolean notFound = false ; 
		
	    for (int i = 0; i < 10 && !notFound; i++) {
	    	
	        for ( int j = 0; j < 10 &&  !notFound ;  j++) {
	        	
	            System.out.println (" inner loop") ; 
	            notFound = true ; 
	           }
	        
	       System.out.println (" out loop") ; 
	      }
	}

	
	public static void main(String[] args) {
//		Scanner keyboard = new Scanner(System.in);
//
//		System.out.println("Type a number that represents your lucky day");
//		int luckyDay = keyboard.nextInt();
//
//		switch (luckyDay) {
//		case 1:
//			System.out.println("Your luck day is Monday");
//			break;
//		case 2:
//			System.out.println("Your luck day Tuesday");
//			break;
//		case 3:
//		case 4:
//		case 5:
//			System.out.println("Your luck day is Wednesday, Thursday  or  Friday");
//
//			System.out.println("is acceptable.");
//			break;
//		default:
//			System.out.println("Your luck day is either Saturday  or Sunday ");
//			break;
//		}
		int  x= 5, y =8 ; 
		System.out.println ( x< y) ; 
	}
}
