import java.util.*;
public class StrToInteger {

	public static void main(String[] args) {
	
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter 5 Numbers to Convert into Integer in String");

	String a = sc.next();
	String b = sc.next();
	String c = sc.next();
	String d = sc.next();
	String e = sc.next();
	
	System.out.println("Input type is :"+a.getClass().getName());
	
	try{		
	
		Integer ai = Integer.parseInt(a);
		Integer bi = Integer.parseInt(b);
		Integer ci = Integer.parseInt(c);
		Integer di = Integer.parseInt(d);
		Integer ei = Integer.parseInt(e);
	
		System.out.println("Converted into Integer using Wrapper class");
		System.out.println(ai+" "+bi+" "+ci+" "+di+" "+ei);
		System.out.println("Converted Type :"+ai.getClass().getName());
	
	}catch (NumberFormatException e){
		
		System.out.println("Please enter a Numeric String");
	}



	}
}	
