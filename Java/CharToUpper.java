import java.util.*;

public class CharToUpper {
	public static void main(String[] args){
	
	Scanner sc =  new Scanner(System.in);
	int n = sc.nextInt();
	System.out.println("Enter a String");
	String input = sc.next();
	
	if(input.length() > n){
		input = input.substring(0,n);
	}

	String uppercase = input.toUpperCase();
	System.out.println("Uppecase Character : "+uppercase);
	

	}
}
