import java.util.*;

public class TestLinkedHashSet {
	public static void main(String[] args) {
	
	LinkedHashSet<String> list = new LinkedHashSet<String>();
	list.add("Hello");
	list.add("How");
	list.add("are");
	list.add("you");

	Object arr[] = list.toArray();

	for(Object o : arr){
		System.out.println(o);
	}

	System.out.println(list);
	list.remove("Hello");

	System.out.println(list);
	//list.removeFirst();
	//System.out.println(list);
	
	list.remove(0);
	
	//arr.remove(0);
   	for(Object o : arr){
                System.out.println(o);
        }
	}
}
