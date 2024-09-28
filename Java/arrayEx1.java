import java.util.*;
public class arrayEx1{
		public static void main(String[] args){
   		
		 Scanner sc = new Scanner(System.in);
		 System.out.println("Enter the Size of array");

		int age[];
		int n = sc.nextInt();
		
		for(int i=0; i<n;i++){
		System.out.println("Enter Number in array");
		age[i] = sc.nextInt();
		System.out.println("\n"+age[i]);
		}
	}
}
