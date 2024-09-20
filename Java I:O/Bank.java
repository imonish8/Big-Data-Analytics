interface savingAccount{
	void withdraw(double amt);
	//double interest(double amt1);
	boolean isLoan();
	
}

interface currentAccount{
	void deposit(double amt);
	
}

class BankServices implements currentAccount, savingAccount{
	 double amt1;
	 double dep;
	 double w;
	 double bal = 5043.34d;

	
	
	
	public void deposit(double dep){
		System.out.println("Thank you for depositing "+dep+" Amount ");
		bal += dep;
		System.out.println("New BALANCE IS "+bal); 
	}
	public void withdraw(double w){
		if(w < bal){
			if(w > 500){
				System.out.println("Success : "+w+ " Deducted from Your savingAccount");
				System.out.println("Thank you for using BANK SERVICES");
			}else{
				System.out.println("Please enter min 500");
			}
		}else{
		System.out.println("Withdraw Ammount exceeds Balance amount ");
		}
	}
	//public double interest(double amt1){
	//
	//}
	
	public boolean isLoan(){
		if(bal > 5000.03){	
			return true;
		}else{
			return false;
		}
	}
	
	
}

public class Bank {

		public static void main(String[] args){
		
		savingAccount s1 = new BankServices();			
		currentAccount s2 = new BankServices();
	
		s1.withdraw(322d);
		s1.isLoan();
		s2.deposit(5000d);
				   
		}
}
