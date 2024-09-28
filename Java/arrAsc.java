import java.util.*;
public class arrAsc{
		public static void main(String[] args){
	
			Scanner sc = new Scanner(System.in);
			System.out.println("Please enter Length of the array");
			
			int n = sc.nextInt();
		
			int arr[] = new int[n];
			
			for(int i =0; i < n ; i++){
				System.out.println("Enter value :");
				arr[i] = sc.nextInt();
			}
			
			System.out.println("Original Order "+Arrays.toString(arr));
			
			int temp;
			
			for(int i = 0; i< n;i++){
				for(int j = i+1; j < n; j++){
		
				if( arr[i] > arr[j]){
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			    }
					
			}
	
	/* 
loop will end before the sorting is completed, so need another loop here
				if(arr[i] > arr[i+1]){
					temp = arr[i];
					arr[i] = arr[i+1];
					arr[i+1] = temp;
				}
			}
			*/
			

			System.out.println("Ascending array "+Arrays.toString(arr));
	}
}

				
