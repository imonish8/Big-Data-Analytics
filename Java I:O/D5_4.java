public class D5_4{
		
		static int searchElement(int arr[],int Element){
			int i;
			for(i = 0; i< arr.length; i++){
				if(arr[i] == Element){
					return i;
				}
			}
		return i;
		}
		public static void main(String[] args){
			int arr[] = {1332, 3232, 242, 222};
			int found = searchElement(arr, 222);
			if(found != -1){
				System.out.println("Element found at: "+found);
			}else{
				System.out.println("Element out of Range -1");
			}
		}	
}
