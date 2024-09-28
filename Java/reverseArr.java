import java.util.*;
public class reverseArr{

			public static void main(String args[]){
		
			Scanner sc =  new Scanner(System.in);
		 	int n = sc.nextInt();
			int arr[] = new int[n];

			System.out.println("Please enter length of the array");
		
			//int n = sc.nextInt();
			for(int i = 0; i<n ; i++){
				System.out.println("Enter value for "+i+"th Index");
				arr[i] = sc.nextInt();
			}
			int revarr[] = new int[n];

			for(int i = 0; i<n ;i++){
				revarr[i] = arr[n-i-1];
			}
			System.out.println(Arrays.toString(revarr));
	}
}
