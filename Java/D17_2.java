import java.util.*;
public class D17_2{
	public static void main(String[] args){

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your String");
		String ustr = sc.nextLine();
		
		StringTokenizer st = new StringTokenizer(ustr, ",");
		
		while(st.hasMoreTokens()){
			System.out.println(st.nextToken());
		}

	}
}
