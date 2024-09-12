public class D5_1{
                static int findIndex(int arr[], int target){
			int i;
			for(i = 0;i<arr.length;i++){
				if(arr[i] == target){
					return i;
				}
			}
			return i;	
		}
		public static void main(String[] args){
			int arr[] = {11,35,64,642,6432,245,224};
			int len = arr.length;
			int found = findIndex(arr, 245);
			if(found != -1){
				System.out.println("Index Found at: "+found);
			}else{
				System.out.println("Index out of Range");
			}
		}
}
			
