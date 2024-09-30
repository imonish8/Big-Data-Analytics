import java.util.*;
public class TestTreeSet {

	public static void main(String[] args) {

	TreeSet<String> set = new TreeSet<>();
	
	set.add("Banana");
	set.add("Apple");
	set.add("Orange");
	
	for(String fruit : set) {
		System.out.println(fruit);
	}
	}
}
