import java.util.*;
public class GetterSetter {

    public static void main(String args[])
    throws ClassNotFoundException
    {
      Scanner sc = new Scanner(System.in);
      System.out.println("Enter name");
      String name = sc.next();
      System.out.println("Enter acc no");
      int accno = sc.nextInt();
      System.out.println("Enter Amount");
      double amt = sc.nextDouble();
      AccountOne obj = new AccountOne();
    //Account obj = new Account();
      obj.setAccno(accno);
      obj.setAmt(amt);
      obj.setName(name);
      
      System.out.println("Enter CHoice");
      System.out.println("D-Deposit , W-Withdraw");
      char choice = sc.next().charAt(0);
      switch(choice) {
        case 'D' :
            obj.deposit(amt);
            obj.Display();
          break;
        case 'W' :
            obj.withdraw(amt);
            obj.Display();
          break;
        default :
            System.out.println("D / W");
          break;
      }
    
    }
  }
  
  class AccountOne {
        int accno; double amt;String name; double bal;
        AccountOne(int accno, double amt, String name){
      //Account(int accno, double amt, String name) {
          this.name= name;
          this.accno = accno;
          this.amt = amt;
        }
        
        AccountOne(){
        
        }
        
        public void setAccno(int accno){
          this.accno = accno;
          }
        public int getAccno(){
          return accno;
        }
        public double getAmt(){
          return amt;
        }
        public void setAmt(double amt){
          this.amt = amt;
        }
        
        public void setName(String name){
          this.name = name;
        }
        
        public String getNAme(){
          return name;
        }
        
        void Display() {
          System.out.println("User's Accountno is"+accno);
          System.out.println("User's Name is "+name);
          System.out.println("User'sBALANCE:"+bal);
          
        }
        void deposit(double amt){
          bal += amt;
        }
        
        void withdraw( double amt) {
          bal -= amt;
        }
        
 }
