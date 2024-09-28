import java.util.*;
public class D4h{
		public static void main(String[] args){
			Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			int sum = 0;
			for(int i=1;i<n;i++){
				if( i % 2 == 0){
					continue;
				}
			System.out.println(i);
			sum = sum + i;
			}
			System.out.println("Sum of all Odd numbers ranging to "+n+" is "+sum);

		}
}
