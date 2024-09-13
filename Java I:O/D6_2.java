import java.util.*;
public class D6_2{
		public static void main(String[] args){
			System.out.println("Dear User, Please Enter a number for Integrity check");
			Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			
			String integrity = ( n > 0 ) ? ("Number is Positive") : (( n < 0) ? ("Number is Negative") : ("Number is Zero"));
			System.out.println(" The Number Integrity is Being Processed... ");
			System.out.println("In our Integrity Check Number Integrity Check is found to be :"+integrity);
		}
}
