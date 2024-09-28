import java.util.*;
public class D6_3{
		public static void main(String[] args){
		System.out.println("Enter Month (eg., 1,2,3...12 etc.)");
		Scanner sc = new Scanner(System.in);
		int usr = sc.nextInt();
		String January, February, March, April, May, June, July, August, September, October, November, December;
		switch(usr){
		
			case 1 :
				System.out.println("January is a 31 day Month");
			break;
			case 2 :
				System.out.println("February is a 28/ 29 day Month");
			break;
			case 3 :
				System.out.println("March is a 31 Day Month");
			break;
			case  4 :
				System.out.println("April is a 30 day Month");
			
			break;
			case 5 :
				System.out.println("May is a 31 Day Month");
			break;
			case 6 : 
				System.out.println("June is a 30 day month");
			break;
			case 7 :
				System.out.println("July is a 31 day month");
			break;
			case 8 :
				System.out.println("August is a 31 day month");
			break;
			case 9 :
				System.out.println("September is a 30 day month");
			break;
			case 10 :
				System.out.println("Oct is a 31 Day month");
			break;
			case 11 :
				System.out.println("November is a 30 day month");
			break;
			case 12 :
				System.out.println("The last Month of the year you have just entered, and it is 31 Day month as we all know 31 Dec Memories");
			break;
			default:
				System.out.println("Dear, please enter a valid Input to proceed with Outputs");
			break;
		}		

		}
}
