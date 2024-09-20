//INHERITANCE HEIRARCHY AND MULTILEVEL
import java.util.*;
class StudentDB{
	String sname, cname, loc;
	int sid;
	byte cid;
	StudentDB(String sname, int sid, String loc, String cname, Byte cid){
                        this.sname = sname;
                        this.sid = sid;
                        this.cname = cname; 
                        this.cid = cid;
                        this.loc = loc;
                }
	
	StudentDB(){
                        
			Scanner sc = new Scanner(System.in);
                        System.out.println("Enter Name");
			sname = sc.next();
			System.out.println("Enter Student ID");
                        sid = sc.nextInt();
			System.out.println("Enter Student Location :");
                        loc = sc.next();   
			System.out.println("Enter Course Name : ");
                        cname = sc.next();
			System.out.println("Enter Course ID");
                        cid = sc.nextByte();
                }
	

	void Display(){
			System.out.println("Student Name is : "+sname);
			System.out.println("Student ID is  : "+sid);
			System.out.println("Student Location is : "+loc);
			System.out.println("Student Course name is :"+cname);
			System.out.println("Student Course ID is : "+cid);
			
	}	
}

class Student1{
		Student1(String sname, int sid, String loc, String cname, Byte cid){
			//super();
		}
		Student1(){
			//super();
		}
		void Display(){
			//super.Display();
		}
}
	

public class OOPinheritance {
	
			public static void main(String[] args){
			StudentDB superObj = new StudentDB();
			superObj.Display();
			}
}
