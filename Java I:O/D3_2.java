import java.util.*;
public class D3_2{
		public static void main(String[] args){
			Scanner sc = new Scanner(System.in);
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			int d = sc.nextInt();

			int greatest = (a >b)
				   ? (a > c)
				      ? (a > d ? a : d)
					: (c > d ? c : d)
				   : (b > c)
				       ? (b > d ? b : d)
					: (c > d ? c : d);

		  System.out.println("Greatest Integer out of " +a+" "+b+ " "+c+" "+d+" "+"is "+greatest);

}
}					
