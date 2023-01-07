package lesson03;

import java.util.ArrayList;
import java.util.Iterator;

public class UsingBreakAndContinue {

	public static void main(String args[]) {

		// for loop without break
		for (int i = 0; i < 3; i++) {

			for (int j = 0; j < 3; j++) {
				System.out.println(i + " , " + j);

			}
		}

		System.out.println("for loop with break in internal loop");

		for (int i = 0; i < 3; i++) {

			for (int j = 0; j < 3; j++) {
				System.out.println(i + " , " + j);
				break;

			}
		}

		System.out.println("for loop with break  and lable in internal loop");

		endBothLoops: for (int i = 0; i < 3; i++) {

			for (int j = 0; j < 3; j++) {
				System.out.println(i + " , " + j);
				break endBothLoops;

			}
		}

		System.out.println("for loop with the continue");
		for (int i = 0; i < 3; i++) {

			for (int j = 0; j < 3; j++) {

				if (i >= 1)
					continue;
				System.out.println(i + " , " + j);

			}
		}

		ArrayList list = new ArrayList();
		for (int i = 0; i < list.size(); i++) {
			String s = (String) list.get(i);
			// do something with s
		}

		// Alternatively, using Iterator would be:

		Iterator<String> itr = list.iterator();
		while (itr.hasNext()) {
			String s = (String) itr.next();
		}

		double database_version = 1.2 ; 
		assert database_version == 1.2 ; 
	}
}
