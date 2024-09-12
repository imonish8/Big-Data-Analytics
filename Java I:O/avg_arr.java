public class avg_arr{
		public static void main(String[] args){
		int arr[] = {1,2,3,4,5};
		int sum =0;
		int len = arr.length;
		for(int i =0;i<arr.length;i++){
			sum = sum + arr[i];
		}
		int avg_sum = sum / len;
		System.out.println("Average is: "+avg_sum);
	}
}
