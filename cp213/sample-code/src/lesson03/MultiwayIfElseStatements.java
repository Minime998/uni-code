package lesson03;

public class MultiwayIfElseStatements {

	public static void main(String args[]) {
		int number = 1234;
		if (number < 100 && number >= 1) {
			System.out.println("Its a two digit number");
		} else if (number < 1000 && number >= 100) {
			System.out.println("Its a three digit number");
		} else if (number < 10000 && number >= 1000) {
			System.out.println("Its a four digit number");
		} else if (number < 100000 && number >= 10000) {
			System.out.println("Its a five digit number");
		} else {
			System.out.println("number is not between 1 & 99999");
		}
	}
}
