import java.util.*;
class Account {
	int accno;String name;double balance=33.33, deposit;
	
	Account (int accno, String name, double deposit){
		this.accno = accno;
		this.name = name;
		this.deposit = deposit;
		balance = balance + deposit;
	}
	Account(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your Account NUmber");
		accno = sc.nextInt();
		System.out.println("Enter account Holder's Name");
		name = sc.next();
		System.out.println("Enter Amount to Deposit");
		deposit = sc.nextDouble();
		}
	
	
	void Display(){
		System.out.println("Account number is "+accno);
		System.out.println("Account Holder Name "+ name);
		System.out.println("Current Deposit Amount is :"+deposit);
		System.out.println("FInal Account Balanace is :"+balance);
	}
}

class SavingAccount extends Account {
		String accType;
		SavingAccount(){
		}
	
		void Display(){
		}
}

class DematAccount extends Account {
		DematAccount(){
		}
		
		void Display(){
		super.Display();
		System.out.println("THis is Demat ACCOUNT");
		}
}







public class D11_1 {
		public static void main(String[] args){
			Account obj_demat = new DematAccount();
			obj_demat.Display();
		}
}
