import java.util.*;
public class novariableswapping{

		public static void main(String[] args){
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter value for x");
			int x = sc.nextInt();
			System.out.println("Enter value for y");
			int y = sc.nextInt();
			
			x = x + y;
			y = x - y;
			x = x - y;
		
			System.out.println("Value for x is :"+x);
			System.out.println("Value for y is :"+y);
		}
}
