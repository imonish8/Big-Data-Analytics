import java.util.*;
public class switchX{
		public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int usr_choice = sc.nextInt();
		
		
		String dayString = "";
		
		switch(usr_choice){
		
		case 1:
			dayString = "Monday";
			break;
		case 2: 
			dayString = "Tuesday";
			break;
		case 3:
			dayString = "Wednesday";
			break;
		case 4:
			dayString = "Thursday";
			break;
		case 5:
			dayString = "Friday";
			break;
		case 6: dayString = "Saturday";
			break;
		case 7: dayString = "Sunday";
			break;
		default:
			System.out.println("Please enter a number ranging from 1 to 7 only");
			break;
		}
		
		System.out.println("You choice of Weekday/Weekend is: "+ dayString);



			
		}
}
