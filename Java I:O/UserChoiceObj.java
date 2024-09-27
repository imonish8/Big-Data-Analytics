import java.util.*;
public class UserChoiceObj {
  
    public static void main(String [] args) {
       
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter name");
        String name = sc.next();
        System.out.println("Enter account number");
        int accno = sc.nextInt();
        System.out.println("Enter initial deposit");
        double amt = sc.nextDouble();
        
        Account obj = new Account(name, accno, amt);
       
        System.out.println("Please enter your choice");
        System.out.println(" D - Deposit, W - Withdraw");
        char choice = sc.next().charAt(0);
        switch(choice) {
          case 'D' :
            obj.deposit(amt);
            obj.display();
            break;
          case 'W' :
            obj.withdraw(amt);
            obj.display();
            break;
          default:
            System.out.println("W / D ");
            break;
        }
      }
}

class Account {
  private String name;
  private double amt;
  private int accno;
  double bal;
  
      public Account(String name, int accno, double amt){
        this.name = name;
        this.bal = bal;
        this.accno = accno;
        }
      void display() {
      System.out.println();
      System.out.println("User's Name is : "+name);
      System.out.println("User's Account Number is "+accno);
      System.out.println("User's Balance is :"+bal);
      System.out.println("THank you for Using Services ");
      System.out.println();
      }
      
      void deposit(double amt){
      bal += amt;
        
      }
      
      void withdraw(double amt){
      bal -= amt;
      }
}
