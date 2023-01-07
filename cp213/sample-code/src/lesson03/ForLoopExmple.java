package lesson03;

public class ForLoopExmple {

	public static void multipleInitialization() {
		double x = 1.0 / 3;

		for (int i = 0, j = 0; x != 0.33333; i++) {
			j++;
			System.out.println("i and j " + i + " " + j);

		}
	}

	public static void multipleupdate() {

		double x = 1.0 / 3;

		if (x == 0.33333)
			for (int i = 0, j = 0; (i + j) < 6; i++, j++, System.out.println("i and j " + i + " " + j))
				;

	}

	public static void main(String args[]) {

//		for (int i = 0; i < 3; i++)
//			System.out.println(" i is " + i);
//
//		int j = 0;
//		for (int i = 0; i < 3; i++) {
//			j += 1;
//			System.out.println(" hello " + j);
//			System.out.println(" j is " + j);
//		}
		// multipleInitialization();
		// multipleupdate() ;

		int rowNum, columnNum;
		for (rowNum = 1; rowNum <= 3; rowNum++) {
			for (columnNum = 1; columnNum <= 2; columnNum++) {
				System.out.print(" row " + rowNum + " column " + columnNum);
			}
			     System.out.println();
		}
	}
}
