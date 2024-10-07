import java.util.*;
public class TestArrayList {
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<>();


		// ADDING
		list.add("Hello");
		list.add("World");
		list.add("JAVA");
		list.add("ACTS");
		
		// .GET
		System.out.println("First element is :"+list.get(0));
		System.out.println();
		System.out.println("Printing all elements after 'add' method");
		System.out.println();
		
		// .ADD(INDEX, ELEMENT)
		list.add(1, "Mango");
		System.out.println("After adding Mango at index 1 :"+list);
		System.out.println();
		
		//.SET(INDEX, ELEMENT)
		list.set(0, "Strawberry");
		System.out.println("After setting strawberry at index 0 : "+list);
		System.out.println();
		
		// .REMOVE(ELEMENT)
		list.remove("Mango");
		System.out.println("After removing element mango "+list);
		System.out.println();
		
		// .REMOVE(INDEX)
		list.remove(3);
		System.out.println("After .remove(index=3) "+list);
		System.out.println();
		

		//.CLEAR DELETES LIST AS IF IT NEVER EXISTED
		//.ISEMPTY CHECKS FOR THE LIST IS EMPTY OR NOT.
		
		//.INDEXOF(OBJECT O)
		int indexof = list.indexOf("JAVA");
		System.out.println("After returning the index java "+indexof);
		
		//.addALL(COLECTION)
		ArrayList<String> fruits = new ArrayList<>();
		fruits.add("Apple");
		fruits.add("samsung");
		fruits.add("nokia");
		fruits.add("sony");
		fruits.add("pineapple");
		System.out.println("After creating fruits ArrayList :"+fruits);
		System.out.println();
		list.addAll(fruits);
		System.out.println("extending list with fruits using .addAll()"+list);
		System.out.println();

		//.SORT(COMPARATOR.NATURALORDER())
		list.sort(Comparator.naturalOrder());
		System.out.println("List after operating using .sort() :"+list);
		System.out.println();
		
		//Converting using Object
		Object [] listarr = list.toArray();
		System.out.println("After converting the list to listarr using Object []");
		for(Object member : list){
			System.out.println(member);
		}
		System.out.println();
			
		//FOR EACH
		list.forEach(member -> System.out.println(member));
		System.out.println();

		
		

		//.SIZE() RETURNS SIZE OF ARRAYLIST
		int size = list.size();
		System.out.println("Checking size of list using :"+size);
		
	
		
		Iterator itr = list.iterator();
	
		while(itr.hasNext()){
			System.out.println(itr.next());
		}
	}
}
