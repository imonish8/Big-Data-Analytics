import java.util.*;
class course_data{
		int idc;
		String namec;
		String institute;
		String review;
		
		course_data(){
			Scanner sc = new Scanner(System.in);
			System.out.println("Hello there !, Please enter course ID");
			idc = sc.nextInt();
	
			System.out.println("Good Job, Now enter Name of the Course");	
			namec = sc.next();
			
			System.out.println("Now proceed with Institute Name");
			institute = sc.next();

			System.out.println("Thank you for providing the Details, Please give review");
			review = sc.next();
			}
		
		course_data(int idc, String namec, String institute, String review){
			this.idc = idc;
			this.namec = namec;
			this.institute = institute;
			this.review = review;		
		}
		void display(){
			System.out.println();
			System.out.println("Here is Summary for the Inputs, which you had just entered");
			System.out.println("ID of the Course: "+idc);
			System.out.println("Name of the Course is: "+namec);
			System.out.println("Institutes of the course : "+institute);
			System.out.println("The Review you have is here : "+review);
		}

}
public class Course{
		public static void main(String[] args){
			//no params
			course_data data1 = new course_data();
			data1.display();
			
			//params
			course_data data2 = new course_data(001, "Big Data Analytics", "CDAC-CHENNAI", "Best of Best");
			data2.display();
		}
}
