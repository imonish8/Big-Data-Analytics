public class acending_arr{

		public static void main(String[] args){
			int arr[] = {1,4,5,63,32,58};
			
			int temp =0;
			
			System.out.println("Elements of original Array: ");
			for(int i=0;i<arr.length;i++){
				System.out.println("Elements original are: "+arr[i]+ " ");
				
			}			
			for(int i = 0;i<arr.length;i++){
				for(int j = i+1; j<arr.length;j++){
			
					if(arr[i] > arr[j]) {
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;	
					}
				}	
			}	
			System.out.println();
			System.out.println("Elements after sorting Array in ascending order here: ");
			for(int i=0;i< arr.length;i++){
				System.out.println(arr[i] + " ");
			}
	}
}
