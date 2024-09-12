public class for_loop{
		public static void main(String[] args){
			int arr[] = {1,2,3,4,5,6,7,8,9,10};
			for(int i=0;i<10;i++){
				
				System.out.println(arr[i]);
				}
				System.out.println("\n");
			for(int i:arr){
				System.out.println(i);
			}
			String str[] = {"Hello", "World"};
			for(String val:str){
			System.out.println(val);
			}
	}
}
