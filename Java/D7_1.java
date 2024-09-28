import java.util.*;
class student {
		int rollcall;
		String name;
		String address;
		long phnumber;

		student(){
			Scanner sc = new Scanner(System.in);
			System.out.println("Dear user, Enter Roll Number of the Student");
			rollcall = sc.nextInt();
			System.out.println("User, please enter First Name of the student");
			name = sc.next();
			System.out.println("Please enter City the student stays");
			address = sc.next();
			System.out.println("Please enter Active Mobile number of the Student");
			phnumber = sc.nextLong();
			}

		void display(){
			System.out.println();
			System.out.println("The entered Values for roll no is: "+rollcall);
			System.out.println("Name of the you've just entered is: "+name);
			System.out.println("The City,  "+name+" is currently residing is: "+address);
			System.out.println("Active Mobile number of "+name+" is "+phnumber);
			}	
}

public class D7_1{
		public static void main(String[] args){
			student object1 = new student();
			object1.display();
		}
}
