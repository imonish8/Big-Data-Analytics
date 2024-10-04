import java.util.*;
interface Account {
	void holder(int accno, String name, double amt);
	
	default void Display(){
		if(this.getClass() == Saving.class){
			System.out.println("This is Saving account & Below is the information for saving account");
		}
		if(this.getClass() == Current.class){
			System.out.println("Thi is Current Account");
		}
	}
}

class Saving implements Account{
		int accno;
		String name;
		double amt;
		double bal = 1000.32d;
		public void holder(int accno, String name, double amt){
			this.accno = accno;
			this.name = name;
			this.amt = amt;
			bal += amt;
		
		}
		
		public void Display(){
			System.out.println("The Account Holder's Name is :"+name);
			System.out.println("The Account Holder's No is : "+accno);
			System.out.println("The Account Holder's Amt to be Deposited is :"+amt);
			System.out.println(name+" Has "+bal+" in Rs as Saving Available Balance");
		}
}

class Current implements Account {
		int accno;
                String name;
                double amt;
                double bal = 50000.22d;
                public void holder(int accno, String name, double amt){
                        this.accno = accno;
                        this.name = name;
                        this.amt = amt;
                        bal += amt;
                 
                }
                
                public void Display(){
                        System.out.println("The Account Holder's Name is :"+name);
                        System.out.println("The Account Holder's No is : "+accno);
                        System.out.println("The Account Holder's Amt to be Deposited is :"+amt);  
                        System.out.println(name+" Has "+bal+" in Rs as Current Available Balance");
                }

		
}
public class InterAccount {
	public static void main(String[] args){
		Account obj_saving = new Saving();
		obj_saving.holder(22222, "Ayush", 3033d);
		obj_saving.Display();
							
	}
}


