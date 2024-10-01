import java.util.*;

public class TestCollections1 {
	public static void main(String[] args){
	
	SortedSet<Integer> ss = new TreeSet<>();
	Random rd = new Random();
	for(int i = 0; i< 50; i++){
		ss.add(rd.nextInt(100));
	}
	System.out.println(ss);
	TreeSet<Integer> tsx = (TreeSet<Integer>) ss.subSet(25, 50);
	System.out.println("SubSet of Random Numbers  \n"+tsx);

	}
}
	
	
