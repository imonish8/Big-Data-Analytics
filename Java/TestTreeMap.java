import java.util.*;

public class TestTreeMap {

	public static void main(String[] args){

	TreeMap<Integer, String> tmap = new TreeMap<>();
	tmap.put(1, "Apple");
	tmap.put(2, "Windows");
	tmap.put(3, "Linux");
	tmap.put(4, "Unix");
	tmap.put(5, "Android");
	tmap.put(6, "Blackberry");
	
	System.out.println("Tree Map Elements :"+tmap);
	System.out.println();
	System.out.println("Lowest key "+tmap.firstKey()+"  value : "+tmap.get(tmap.firstKey()));
	System.out.println();
	
	}
}

	
