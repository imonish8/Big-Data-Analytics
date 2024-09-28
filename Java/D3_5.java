import java.util.*;
public class D3_5{
		public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int original = sc.nextInt();
		int userNumber = original;
		int reversed = 0;
		while(original != 0){
		int reminder = original % 10;
		reversed = reversed*10 + reminder;
		original = original / 10;
		
		}
		if(reversed == userNumber){	
			System.out.println("Number is Palindrome");
		}else{
			System.out.println("Number is not Palindrome");
		}
	}
}
