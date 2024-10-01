import java.util.*;
public class testJavaCollection {
	public static void main(String[] args) {

		Deque<String> deque = new ArrayDeque<String>();
		deque.add("Guatum");
		deque.add("Karan");
		deque.add("Ajay");

		deque.addFirst("Added first name");	
		deque.addLast("Added last using method");
		
		deque.removeFirst();
		deque.removeLast();
		//deque.remove("Karan")
		System.out.println("deque.contains() Mathod :"+deque.contains("Guatum"));

		System.out.println("deque.isEmpty() method :"+deque.isEmpty());
		System.out.println("deque.peek() method :"+deque.peek());
		for(String str : deque){
			System.out.println(str);
		}




	}
}
