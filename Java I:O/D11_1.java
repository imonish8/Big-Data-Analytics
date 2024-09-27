import java.util.*;
class Account {
	int accno;String name;double balance=0;double amt;
	
	Account (int accno, String name){
		this.accno = accno;
		this.name = name;
		
	}
	
	void deposit(){
	    balance += amt;
	    }
	void withdraw(){
	    balance -= amt;
	    }
	Account(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your Account NUmber");
		accno = sc.nextInt();
		System.out.println("Enter account Holder's Name");
		name = sc.next();
		System.out.println("Enter Amount to Deposit");
		amt = sc.nextDouble();
		}
	
	
	void display(){
		System.out.println("Account number is "+accno);
		System.out.println("Account Holder Name "+ name);
		System.out.println("Current Deposit Amount is :"+amt);
		System.out.println("FInal Account Balanace is :"+balance);
	}
}

class SavingAccount extends Account {
		String accType;
		SavingAccount(){
		}
	
		void display(){
		super.display();
		}
		void deposit(){
	  super.deposit();
	    }
	void withdraw(){
	    super.withdraw();
	    }
}

class DematAccount extends Account {
		DematAccount(){
		}
		
		void display(){
		super.display();
		System.out.println("THis is Demat ACCOUNT");
		}
		void deposit(){
	  super.deposit();
	    }
    void withdraw(){
	  super.withdraw();
	    }
}







public class D11_1 {
		public static void main(String[] args){
			Account obj = new DematAccount();
			
			Scanner sc = new Scanner(System.in);
			
			System.out.println("Please enter W / D");
			char choice = sc.next().charAt(0);
			
			switch(choice) {
			  case 'D' :
			        obj.deposit();
			        obj.display();
			        break;
			  case 'W' :
			        obj.withdraw();
			        obj.display();
			        break;
			  default :
			        System.out.println("Enter VAlid inputs");
			        break;
			  
			
			}
			
		}
}
