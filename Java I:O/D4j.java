import java.util.*;
public class D4j{
		public static void main(String[] args){
			Scanner sc = new Scanner(System.in);
			int year = sc.nextInt();
			
			if(year % 4 == 0){
				if(year % 100 ==0){
					if(year % 400 == 0){
						System.out.println("Year Leap");
					}else{
					System.out.println("Year is not leap");
					}
				
				}else{
				System.out.println("Year not leap");
				}	
			 }else{
			 System.out.println("Year is not leap");
			 }
		}
}
