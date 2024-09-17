import java.util.*;
public class palindrome{
		public static void main(String[] args){
			System.out.println("Enter the number");
			Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			int sum = 0,r;
			int temp = n;
			while(n>0){
				r = n%10; //getting reminder
				sum=(sum*10)+r; // adding to reversed number which sum of reminder + 10sum
				n = n/10;
			}
			if(temp == sum)
				System.out.println("Palindrome Number");	
			else
				System.out.println("Not a Palindrome");
			
		}
}
