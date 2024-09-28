import java.util.*;
public class TextException{
		public static void main(String[] args){	
			try{
				Scanner sc = new Scanner(System.in);			
				int numbers[] = {1,2,3,4};
				//io exception
				int Element = sc.nextInt();
				System.out.println(numbers[4]);
			 	System.out.println("Enter Numbers");
				
				//arithmatic exception
		
					float a = sc.nextInt();
                                        float b = sc.nextInt();
                                        float res =  a/b;
				System.out.println("Answer is "+res); 
		// exception e will handle any error and print whatever.				
	   		}catch (Exception e){
					System.out.println("Exception e catch block is being executing");
					
					System.out.println("Please enter two numbers");
					System.out.println("Coding Exceptions"+e.getMessage());
					
			}
			/*catch (ArithmeticException ae){
				System.out.println("Monish, you've made arithmetic Logic wrong");
				

			}*/
		}
}
