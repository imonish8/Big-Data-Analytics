import java.util.*;
import java.io.*;

public class TestException2 {

		
		public static void main(String[] args) 
		throws Exception 
		{
		
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			String str = br.readLine();
			
			FileReader fr = new FileReader("Today.txt");
		
		throw new IOException();
		
		}catch (Exception e){
		
			System.out.println(e.getMessage());

		}
		
		finally {
			System.out.println("Main method finally success");
		
		}
	}
}
				
