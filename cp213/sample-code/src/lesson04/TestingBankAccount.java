package lesson04;

public class TestingBankAccount {

	BankAccount anAccount;

	public void test1() {
		BankAccount myDefaultAccount = new BankAccount();
		System.out.println(myDefaultAccount);
	}

	public void test2() {
		BankAccount myNonEmptyAccount = new BankAccount("123", "AR Yunis", 100);
		System.out.println(myNonEmptyAccount);

	}
	
	
	

	public static void main(String args[]) {
		TestingBankAccount testingAccount = new TestingBankAccount();

		testingAccount.test1();
		testingAccount.test2();

		BankAccount ac = new BankAccount("123", "AR Yunis", 100);
		ac.getCustomer_name();
		String myAcountNumber = ac.getAccountNumber();
		System.out.println(myAcountNumber);
	
		ac.deposit(100); 

	}
	
	

}
