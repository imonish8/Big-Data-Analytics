import java.util.*;
public class D4d{
		public static void main(String[] args){
			Scanner sc = new Scanner(System.in);
			
			System.out.println("Enter a number to check");
			int n = sc.nextInt();
                                      
String check = ( n > 0 ) ? "Positive" : ((n < 0) ? "Negative" : "Zero");
			System.out.println("Number is : "+check);
		}
}
