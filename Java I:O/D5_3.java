public class D5_3{
		static int findElement(int arr[], int element){
			int i;
			for(i = 0;i < arr.length; i++){
				if(arr[i] == element){
					return i;
				}	
			}
		return i;
		}
		public static void main(String[] args){
			int arr[] = {12,34, 53, 532, 5212};
			int found = findElement(arr, 532);
			if(found != -1){
				System.out.println("Element is available at index : "+found);
			}else{
				System.out.println("Element not found, out of range");
			}
		}
}
