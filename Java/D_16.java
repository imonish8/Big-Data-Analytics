import java.util.*;
public class D_16 {
	public static void main(String[] args) {
		
	try{	
	Account acc = new Account(23232, "Ayush", 222299);
	acc.Display();
	
	}catch (Exception e){
	System.out.println("Error has occured "+e.getMessage());
	}
	
	}
}

class Account {
	int accno;
	String name;
	double bal = 5000.22d;
	double amt;
	
	Account(int accno, String name, double amt){
		this.accno = accno;
		this.bal = bal;
		this.name = name;
		this.amt = amt;

		bal += amt;
	}

	void Display(){
		System.out.println("Account holder's Name is :"+name);
		System.out.println("Account Holder's Number is :"+accno);
		System.out.println("Account Holder's Amount to be deposited is :"+amt);
		System.out.println("Account Holder's Balance is "+bal);
	}
}

