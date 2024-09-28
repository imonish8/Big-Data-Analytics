import java.util.*;
class Customer{
	int cid;
	String cname;
	Scanner sc = new Scanner(System.in);
	Customer(){
		System.out.println("Enter Customer ID :");
		cid = sc.nextInt();
		
		System.out.println("Enter Customer Name : ");
		cname = sc.next();
			
	}
	
	void Display(){
		System.out.println("Parent class Display method");
		System.out.println("Customer ID is : "+cid);
		System.out.println("Customer Name is : "+cname);
		System.out.println();
	
	}

}

class WholeSaleCustomer extends Customer{
		long accno;
		Scanner sc = new Scanner(System.in);
		WholeSaleCustomer(){
			super();
			System.out.println("Enter Customer Account no: ");
			accno = sc.nextLong();
		}
		

		void Display(){
			super.Display();
			System.out.println("subclass Wholesalecustomer obj");
			System.out.println("Account no of the Customer is : "+accno);
			System.out.println();

		}
	}

class RetailCustomer extends Customer{
		long accno;
		Scanner sc = new Scanner(System.in);
		RetailCustomer(){
			super();
			System.out.println("Enter Account no for Retail Customer : "+accno);
		}
		
		void Display(){
			super.Display();
			System.out.println("Subclass Retailcustomer obj loading");
			System.out.println("Retail Customer account no is : "+accno);
			System.out.println();
		}
	}

public class D10 {

		public static void main(String[] args){
			
			Customer class_obj = new Customer();
			class_obj.Display();

			RetailCustomer subclass_obj1 = new RetailCustomer();
			subclass_obj1.Display();

			WholeSaleCustomer subclass_obj2 = new WholeSaleCustomer();
			subclass_obj2.Display();
	
		}
}
