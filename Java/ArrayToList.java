import java.util.*;
public class ArrayToList {

	public static void main(String[] args) {
		Integer a[] = {10,20,30,40,50};
		ArrayList<Integer> alist = new ArrayList<>(Arrays.asList(a));
		
		Object arr[] = alist.toArray();
		
		for(Object o : arr){
			System.out.println(o);
		}
	
		for(Integer  a1 : a){
			System.out.println(a1);
		}

		System.out.println(alist);
		System.out.println(alist.get(2));	
		Collections.addAll(alist, a);
		System.out.println(alist);

	}
}
