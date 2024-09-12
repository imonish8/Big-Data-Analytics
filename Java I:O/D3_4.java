import java.util.*;
public class D3_4{
		public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a number ");
		int num = sc.nextInt();
		boolean flag = true;
		for(int i=2;i<num;i++){
			if((num % i == 0) || (num % (i+2) == 0)){
				flag = false; 
			} 
			else{
			flag = true;
			}
		}		
		if(flag){
			System.out.println("The number is Prime");
		}
		else{
			System.out.println("The number is not prime");
		}
	}
}
