import java.util.*;
public class simpleInput{
		public static void main(String[] args){
			Scanner sc = new Scanner(System.in);			

			System.out.println("Enter a string");	
			String usrStr;
			usrStr = sc.nextLine();
		
			System.out.println("Enter Intger");
			int usr0;
			usr0 = sc.nextInt();

			// float
			System.out.println("Enter a Float Number");
			float usr1;
			usr1 = sc.nextFloat();
			
			//BYTE
			System.out.println("Enter a Byte number");
			byte usr2;
			usr2=sc.nextByte();
			
			//double
			System.out.println("Enter Double");
			double usr3;
			usr3 = sc.nextDouble();
			
			System.out.println("\n" +" "+usrStr+" "+ usr0+" "+ usr1+" "+ usr2+" "+ usr3);
								
		}
}
