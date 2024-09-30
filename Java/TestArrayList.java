import java.util.*;
public class TestArrayList {
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<>();

		list.add("Hello");
		list.add("World");
		list.add("JAVA");
		list.add("ACTS");
		
		System.out.println("First element is :"+list.get(0));

		Iterator itr = list.iterator();
	
		while(itr.hasNext()){
			System.out.println(itr.next());
		}
	}
}
