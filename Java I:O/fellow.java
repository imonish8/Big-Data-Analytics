import java.util.*;
class fellow_dt{
		int regNum;
		long mbnum;
		String address;
		String name;
		
		//no params.	
		fellow_dt(){
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter you name");
			name = sc.next();
			
			System.out.println("Enter your Register Number: ");
			regNum = sc.nextInt();
	
			System.out.println("Enter your Mobile Number: ");
			mbnum = sc.nextLong();

			System.out.println("Enter your Address: ");
			address = sc.next();
		
			}
		// with params
		fellow_dt(int regNum, long mbnum, String address, String name){
		this.regNum = regNum;
		this.mbnum = mbnum;
		this.address= address;
		this.name = name;
		}
		
		void display(){
		System.out.println("Fellow's Name is: "+name);
		System.out.println("Fellow's Reg.No is: "+regNum);
		System.out.println("Fellow's mbnum is : "+mbnum);
		System.out.println("Fellow's address is : "+address);	

		}
}
public class fellow{
		public static void main(String[] args){
		
		fellow_dt Obj1 = new fellow_dt();
		Obj1.display();
		
		//fellow_dt obj_params = new fellow_dt(111,9898989898l,"Pune","Ganesh");
		//obj_params.display();
		
		}
}
		
