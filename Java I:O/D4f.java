import java.util.*;
public class D4f {
		public static void main(String[] args){
				Scanner sc = new Scanner(System.in);
				System.out.println("please enter first number");
				int a = sc.nextInt();
				System.out.println("Please enter second number");
				int b = sc.nextInt();
				System.out.println("Please enter third number");
				int c = sc.nextInt();

			int great = (a > b) ? ((b > c ) ? a : b) : c;
				System.out.println("greatest number out of three is: "+great);
	

		}
}
