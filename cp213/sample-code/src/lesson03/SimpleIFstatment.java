package lesson03;

public class SimpleIFstatment {

	public static void main(String args[]) {

		int mark = 0;

		if (mark > 85)
			System.out.println(" Your grad is A");
		else
			System.out.println(" Your grad is not A");

		int myScore = 100, yourScore = 50, wager = 0;

		if (myScore > yourScore) {
			System.out.println("I win!");
			wager = wager + 100;
		} else {
			System.out.println("I wish these were golf scores.");
			wager = 0;
		}

		double weight = 100, ideal = 55, calorieIntake = 1200, excersieRate = 20;

		if (weight > ideal)
			calorieIntake = calorieIntake - 500;

		if (weight > ideal) {
			calorieIntake = calorieIntake - 500;
			System.out.println(" your excersie reat need to increase") ; 
			excersieRate = excersieRate * 1.3;
        }
		
		
//		
//		if (a > b) {
//			
//			if (c > d) {
//				
//				if ( g < h) {
//					// code
//				}
//			}
//		}else if (m == n) {
//			
//			if ( z > y) {
//				// code 
//			}
//		}

	}
}
