import java.util.*;
import java.io.*;
	
public class TestException2 {

		
		public static void main(String[] args) 
		// This should be catched by Catch block. or else program will terminate.
		//throws Exception 
		{
		
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
			
			System.out.println("Enter a Number");
			
			//IOException here
			String usr = br.readLine();
			
			//NumberFormatException here.
			int id = Integer.parseInt(usr);
			System.out.println(id);
			
			
			FileReader fr = new FileReader("Todat.txt");
		
		//explicitly Throwing it, but wont print.
		//throw new IOException();
		
		}catch (IOException io){
		
			System.out.println("1st Catch Block Caught it ! "+io.getMessage());

		}catch (NumberFormatException ne){

			System.out.println("2nd Catch block caught it !"+ne.getMessage());
		
		}finally {
			System.out.println("Main, finally success");
		
		}
	}
}
				


// so when you explictly send exception it wont throw exception if there is no,
// error, if there exits any error it will throw.

// So when specific exception like IO or Array, it will get message,
// if passed Exception for all that is Exception e, it will print all exception
//plus the message of it.

// Throw exception is uncalled and uncessary i think.
