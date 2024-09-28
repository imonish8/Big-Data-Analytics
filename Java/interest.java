import java.util.*;
class interest{

	public static void main(String [] args){
			double principle, rate;
		
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter the Princple Amout");	
			
			principle = sc.nextDouble();
			
			System.out.println("Enter a Interest amount");
			rate = sc.nextDouble();
			
			System.out.println("Enter the number of times interest is compounded");
			int n = sc.nextInt();
	
			System.out.println("Enter the number of time Period");
			int t = sc.nextInt();

			double CI = principle*Math.pow((1.0+(rate/n)),(n*t));
			System.out.println("Compound interest Calculated"+CI);
		}
}
