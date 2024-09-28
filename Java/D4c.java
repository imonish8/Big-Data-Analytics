import java.util.*;
public class D4c {
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Please enter a Number for a Table to prepare");
			
			int n = sc.nextInt();
			for(int i=1;i<11;i++){
			System.out.println(n+" "+"X"+i+" "+"="+" "+(i*n));
			
			}
	}
}
