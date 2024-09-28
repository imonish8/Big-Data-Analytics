import java.util.*;
class universityDB{
	int sID; // numbers
	String Discipline; //engineering, medical, arts
	int BldgNo;

	static private int fired = 3;
	
	Scanner sc = new Scanner(System.in);
	
	universityDB(){
		System.out.println("Please Enter Your StudentID to Enter University Database");
		sID = sc.nextInt();
		System.out.println("Please enter Your Discipline as in Engineering, Medical or Arts");
		Discipline = sc.next();
		System.out.println("Please enter Building No. You are in");
		BldgNo = sc.nextInt();
	}
	universityDB(int sID, String Discipline, int BldgNo){
			this.sID = sID;
			this.Discipline = Discipline;
			this.BldgNo = BldgNo;
		}

	void Display(){
		
		System.out.println("The Student ID is : "+sID);
		System.out.println("The Building No is : "+BldgNo);
		System.out.println("The Discipline is : "+Discipline);
		
		
		if(this.getClass() == professors.class){
			System.out.println("The Professors who are going to be fired "+fired);
		}
		
		
	}
}
class departments extends universityDB{
	String dname;
	int did;
	
	departments(String dname, int did){
		//super();
		this.dname = dname;
		this.did = did;	
	}
	departments(){
		super();
		System.out.println("Enter Department Name ; ");
		dname = sc.next();
		System.out.println("Enter Department ID : ");
		did = sc.nextInt();
	}
	
	void Display(){
		super.Display();
		System.out.println("The department name is "+dname);
		System.out.println("Department ID is "+did);
	}

}

class professors extends departments{
	int failed;
	String pname;
	Scanner sc = new Scanner(System.in); 
		professors(){
			super();
			System.out.println("Please enter Professor Name : ");
			pname = sc.next();
		}	
	void  Display(){
			super.Display();
			if(this.getClass() == professors.class){
			System.out.println("Private info to Professor, "+failed+" Student(s) are(is) Failed.");
			}
			System.out.println("Name of the Professor is : "+pname);
		}
}

class campus extends universityDB{
	char YesNo;
		campus(){
			super();
			System.out.println("Please enter Y / N, Are you a Campus Hostel Student or Day Scholar");
			YesNo = sc.next().charAt(0);
		}
	void Display(){
			super.Display();
			System.out.println("You're Response to Hosteller is : "+YesNo);
			if(YesNo == 'Y'){
				System.out.println("You are allowed to Use Library extended period of time");
			}else{
				System.out.println("You are allowed to use Library in Given time Frame only");
			}
		}
			
}


public class University{

		public static void main(String[] args){
				
				//departments obj2 = new departments("Engineering", 2);
				//obj2.Display();
			
				//PRIVATE INFO PROFESSOR.
				//professors  obj1 = new professors();
				//obj1.failed=3;
				//obj1.Display();
			
				//universityDB obj3 = new universityDB();
				//obj3.Display();
				
				departments d1 = new departments();
				
				universityDB u1;
				u1 = d1;
				u1.Display();
				
				//campus c1 = new campus();
 				//c1.Display();
		}
}
