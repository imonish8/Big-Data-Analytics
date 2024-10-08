import java.util.*;
public class D22_1 {
	
	public static void main(String[] args){

	LinkedList<String> fruits = new LinkedList<>();
	
	fruits.add("Apple");
	fruits.add("Orange");
	fruits.add("Pineapple");
	fruits.add("Avocado");


	System.out.println("FOR EACH METHOD USES LAMBDA EXPRESSION TO PRINT");
	fruits.forEach(fruit -> System.out.println(fruit));
	}
}
