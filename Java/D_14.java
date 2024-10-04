import java.lang.reflect.Field;
import java.util.*;

public class D_14 {

	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter five Numerics in String");
		String a = sc.next();
		String b = sc.next();
		String c = sc.next();
		String d = sc.next();
		String e = sc.next();
		
		System.out.println("The String values are :"+a+" "+b+" "+c+" "+d+" "+e);
		
		System.out.println("The type of five inputs you have entered is :"+a.getClass().getName());
		System.out.println("The type of Input you have entered is :"+a+" "+b+" "+c+" "+d+" "+e);
		
		Integer ai = Integer.parseInt(a);
		Integer bi = Integer.parseInt(b);
		Integer ci = Integer.parseInt(c);
		Integer di =  Integer.parseInt(d);
		Integer ei = Integer.parseInt(e);
	
		System.out.println();
		System.out.println("String to Integer Conversion :"+ai+" "+bi+" "+ci+" "+di+" "+ei);
		
		System.out.println("The type of variable is :"+ai.getClass().getName());

	}
}
