import java.util.*;
public class TestStack {

	public static void main(String[] args) {
			
			Stack<String> stack = new Stack<String>();
	
			stack.push("Ayush");
			stack.push("Arnav");
			stack.push("Avinash");	
			stack.pop();
			stack.pop();
			stack.push("Abhijit");
			stack.push("Abhijeet");
		
			Iterator<String> itr = stack.iterator();

			while(itr.hasNext()){

				System.out.println(itr.next());
			}
	}
}
