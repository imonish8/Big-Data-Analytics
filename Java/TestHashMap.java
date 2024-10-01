import java.util.*;
public class TestHashMap {
	public static void main(String[] args) {

	Map<Integer, String> map = new HashMap<>();
	map.put(1, "One");
	map.put(2, "Two");
	map.put(3, "Three");
	map.put(4, "Four");
	map.put(5, "Five");

	//get
	System.out.println("Get method value return"+map.get(1));
	
	//remove using key value pair
	map.remove(2);
	System.out.println(map);
	System.out.println();
	System.out.println(map.size());
	System.out.println();
	System.out.println("Checking contains method "+map.containsKey(3));
	System.out.println();
	System.out.println("Checking ContainsValue method "+map.containsValue("Three"));
	map.putIfAbsent(6, "Six");
	System.out.println();
	map.replace(1, "Apple");
	System.out.println("After replacing with Apple"+map);
	System.out.println();
	System.out.println("Returning true if Emoty "+map.isEmpty());
	
	Set<Integer> keys = map.keySet();
	System.out.println("Keys: "+keys);

	System.out.println(map);
	}
}
