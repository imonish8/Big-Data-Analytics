import java.util.*;
public class D4i{
			int fibonacci(int n){
				if(n<=1){
					return n;
				}
				return fibonacci(n-1) + fibonacci(n-2);

			}
			public static void main(String[] args){
                                Scanner sc = new Scanner(System.in);
				int n = sc.nextInt();
				
				D4i obj = new D4i();
				int res = obj.fibonacci(n);
				
				System.out.println("Fibonacci for number "+n+" is "+res);
			

	}
}
