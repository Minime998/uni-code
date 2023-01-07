package lesson04;

public class BankAccount {

	private String accountNumber = "";
	private String customer_name = "";
	private double balance = 0.0;

	public BankAccount() {
		this.accountNumber = accountNumber;
		this.customer_name = customer_name;
		this.balance = balance;
	}

	/**
	 * constructor for the BankAccount class
	 * 
	 * @param accountNumber unique client account
	 * @param customer_name name of the client
	 * @return new balance is returned
	 */
	public BankAccount(String accountNumber, String customer_name, double balance) {
		super();
		this.accountNumber = accountNumber;
		this.customer_name = customer_name;
		this.balance = balance;
	}

	public BankAccount(String Name) {
		super();
		this.customer_name = Name;

		setAccountNumber(getAccountNumber() + 1);
		;
		setBalance(0.0);

	}


	private boolean isPositive(double amount) {

		return (balance - amount >= 0);
	}

	public double deposit(double balance) {

		balance = balance + balance;
		balance = 500;

		System.out.println(balance);
		return (balance);
	}



public boolean login () {
	return true; 
}

public boolean validate () {
	return true; 
}

public boolean checkRole () {
	return true; 
}

	public double deposit(String accountNumber, double amount) {
		double balance = 0.0;
		if (this.accountNumber == accountNumber)
			balance = balance + amount;

		return (balance);
	}

	public String withdraw(double amount) {
		String newbalance = "";
		if (isPositive(amount)) {
			balance = balance - amount;
			newbalance = "your new blace is" + balance;
		} else {
			newbalance = "you do not have enought fund to withdraw" + amount;
		}
		return newbalance;
	}

	@Override
	public String toString() {

		return (" the account number for the customer " + customer_name + " is " + accountNumber
				+ " and the balance is " + balance);
	}

	public String getAccountNumber() {
		return accountNumber;
	}

	public void setAccountNumber(String accountNumber) {
		this.accountNumber = accountNumber;
	}

	public String getCustomer_name() {
		return customer_name;
	}

	public void setCustomer_name(String customer_name) {
		this.customer_name = customer_name;
	}

	public double getBalance() {
		return balance;
	}

	public void setBalance(double balance) {
		this.balance = balance;
	}

	public void myMethod(int a, int b, double c) {
		a = b + (int) c;
		b = (int) c + a;
		c = a + b;

		System.out.println(" the values of paramters a, b, and c changed inside the method ");
		System.out.println(" a is " + a);
		System.out.println(" b is " + b);
		System.out.println(" c is " + c);

	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((accountNumber == null) ? 0 : accountNumber.hashCode());
		long temp;
		temp = Double.doubleToLongBits(balance);
		result = prime * result + (int) (temp ^ (temp >>> 32));
		result = prime * result + ((customer_name == null) ? 0 : customer_name.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		BankAccount other = (BankAccount) obj;
		if (accountNumber == null) {
			if (other.accountNumber != null)
				return false;
		} else if (!accountNumber.equals(other.accountNumber))
			return false;
		if (Double.doubleToLongBits(balance) != Double.doubleToLongBits(other.balance))
			return false;
		if (customer_name == null) {
			if (other.customer_name != null)
				return false;
		} else if (!customer_name.equals(other.customer_name))
			return false;
		return true;
	}
	
//	public double specialInterstRate  (int disacount) {
//		double primeRate = 4; 
//		System.out.println ("int called and rate is " + primeRate) ; 
//		return (primeRate - disacount ) ; 
//	}
//
//	
	
	public double specialInterstRate  (double disacount) {
		double primeRate = 2.45; 
		System.out.println ("double called and rate is " + primeRate) ; 
		return (primeRate - disacount ) ; 
	}





	public static void main(String args[]) {

		BankAccount baccount1 = new BankAccount();
		System.out.println(baccount1);

		BankAccount baccount2 = new BankAccount("123", "AR", 100.0);
		System.out.println(baccount2);

		String ac1 = baccount1.accountNumber ; 
		String name = baccount1.customer_name ; 
		double balance = baccount1.balance ; 
		
		int a =1, b =2 ; double c = 3.5 ; 
		
		baccount1.myMethod(1, 2, 3);
		
		System.out.println ( " the origianl values of paramters a, b, and c not impacted  "); 
		System.out.println ( " a is " + a ); 		
		System.out.println ( " b is " + b ); 		
		System.out.println ( " c is " + c ); 

		double disAccount = 1 ; 
		baccount1.specialInterstRate(1) ; 
	}

}
