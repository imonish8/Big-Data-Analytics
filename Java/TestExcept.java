import java.util.*;
public class TestExcept{
		public static void main(String[] args){
			try {
				
				Scanner sc = new Scanner(System.in);
				int n = sc.nextInt();
				
				//NumberFormatException
				System.out.println(n);
	
			}
			/*catch (Exception e){
				System.out.println("Coding Exception found");
			}*/
			catch (NumberFormatException ne){
				System.out.println("Trying to get a Message: "+ne.getMessage());

			
			}finally {

				System.out.println("Run Success !");
			}
	}
}
