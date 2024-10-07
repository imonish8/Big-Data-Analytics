// arraylist
import java.util.*;

public class D18_2{
	public static void main(String[] args){
	
	ArrayList<String> fruits = new ArrayList<>();
	fruits.add("Apple");
	fruits.add("Orange");
	fruits.add("Melon");
	fruits.add("Dragon");
	fruits.add("Avocado");
		
	fruits.forEach(fruit -> System.out.println(fruit));
	System.out.println();
	int idx = 0;
	boolean flag = false;
	
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the Fruit to find out in the list");
	String find = sc.next();
	System.out.println();
	

	for(int i = 0; i< fruits.size(); i++){
		if(find.equals(fruits.get(i))){
			idx = i;
			flag = true;
		}
	}

	if(flag == true){
	System.out.println(find+" is found at index "+idx+" is "+flag);
	}else{
	System.out.println("Element not Found");
	}
	

	}
}
