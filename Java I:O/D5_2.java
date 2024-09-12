public class D5_2{
		
		static int findAvgArray(int arr[]){
			int sum = 0;
			for(int i = 0;i< arr.length; i++){
				sum += arr[i];
			}
	
			return(sum / arr.length);
			
		}
		public static void main(String[] args){
			int arr[] = {12, 422, 4214, 24522, 24};
			int avg = findAvgArray(arr);
			System.out.println("The average sum is: "+avg);		
		}
	}
