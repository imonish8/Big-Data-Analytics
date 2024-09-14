import java.util.*;
 class student_data{
		int numRegister;
		String name;
		String address;
		long mnumber;

		void input(){
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter Register Number of the Student");
		numRegister = sc.nextInt();
		
		
		
		System.out.println("Enter Name of the Student");
		name = sc.next();
		
		
		System.out.println("Enter Address for the Student");
		address = sc.next();
		
		System.out.println("Enter Mobile Number for the Student");
		mnumber = sc.nextLong();
		
		}

		String findAddress(){
			return address;
		}	
		
		void Display(){
			System.out.println("Student Name is: "+name);
			System.out.println("Student Mobile number is: "+mnumber);
			System.out.println("Student Regis. Number is: "+numRegister);
		}	
		
}

	class PGStudents extends student_data {
		PGStudents(){
			super();
			
		}
		void Display(){
			super.Display();	
		}
	}
	public class student {

		public static void main(String[] args){
		
		student_data Neel = new student_data();
		
		Neel.input();
		System.out.println("Student address is: "+Neel.findAddress());
		Neel.Display();
		
		System.out.println("\n");
		student_data object2 = new student_data();
		object2.input();
		System.out.println("Student address is: "+object2.findAddress());
		object2.Display();
                
		student_data object3 = new student_data();
		object3.numRegister = 2002;	
		object3.name = "Prabhu";
		object3.mnumber = 909090909l;
		System.out.println(object3.address= "Hyd");
		}
	
}
