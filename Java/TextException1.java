import java.util.*;
import java.io.*;
public class TextException1{
		public static void main(String[] args){	
			try{
				
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
			String str  = br.readLine();

			FileReader fr = new FileReader("today.txt");
	   		
			}catch (IOException ie){
					System.out.println(ie);		
			}
		
		}
}
