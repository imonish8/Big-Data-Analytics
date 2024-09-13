import java.util.*;
class employee{
		int eid;
		String ename;
		String ecity;
		long enumber;
		//constructors without params
		employee(){
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter Employee ID Number in integer");
			eid = sc.nextInt();
			System.out.println("Enter Employee's Name, First Name only");
			ename = sc.next();
			System.out.println("Enter Employee's City, currently Resides.");
			ecity = sc.next();
			System.out.println("Enter Employee's Mobile Number for Record");
			enumber = sc.nextLong();
			}
		// constructors passing params./ protecting data.
		employee(int eid, String ename, String ecity, long enumber){
			
			this.eid = eid;
			this.ecity = ecity;
			this.ename = ename;
			this.enumber = enumber;
			
			}
		// method calling from instance of the object.
		void display(){
			System.out.println();
			System.out.println("Employee name is : "+ename);
			System.out.println("Employee ID is : "+eid);
			System.out.println("Employee's City is : "+ecity);
			System.out.println("Employee's Number is : "+enumber);
			System.out.println();
			
			}
}

public class D7_2{
		public static void main(String[] args){
			// creating object 1. passing params to it.
			employee object1 = new employee(101, "Yashraj", "Mumbai", 989898989l);
			object1.display();
			
			// creating object 2 without passing params.
			employee object2 = new employee();
			object2.display();
		}
}
	
