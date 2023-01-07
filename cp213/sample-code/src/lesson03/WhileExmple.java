package lesson03;

public class WhileExmple {

	public static void main(String[] args) {
		int countDown;

		System.out.println("First while loop:");
		countDown = 5;
		while (countDown > 0) {
			System.out.println("Hello");
			countDown -= 1;
		}

		System.out.println("Second while loop:");
		countDown = 0;
		while (countDown > 0) {
			System.out.println("Hello");
			countDown -= 1;
		}

		System.out.println("First do-while loop:");
		countDown = 5;
		do {
			System.out.println("Hello");
			countDown -= 1;
		} while (countDown > 0);

		
		
		System.out.println("Second do-while loop:");
		countDown = 0;
		do {
			System.out.println("Hello");
			countDown -= 1;
		} while (countDown > 0);
		
	}
}
