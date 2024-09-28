public class swapnums{

	int res;

              	static void swapper(int m, int n){
		System.out.println("Before swapping m is"+m+" and  n is "+n);
		
			int temp = m;
			m = n;
			n = temp;
		System.out.println("After Swapping the numbers are m = "+m+" and for n = "+n);

		}
		
	public static void main(String[] args){
		swapper(4,6);
			
	}
}
