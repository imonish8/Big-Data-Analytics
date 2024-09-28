import java.util.*;
import java.io.*;
class Student extends Exception{

		Student(){
			//System.out.println("Yes Passed !");
			super("Yess passed");
		}
}

public class TestException3{

		public static void main(String[] args){
	
			//Exception e1 = new Student();
			//e1.isPass();
		try             
		{                       
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

			String result=br.readLine();

			if(result.equals("fail"))
				throw new Student();
		}catch (Student ue)
		{
			System.out.println(ue.getMessage());
		}


	}
}
























/*		

import java.io.*;
class UserException extends Exception
{
UserException()
{
super("Not eligible for placements");
}
}

class TestUserException
{
public static void main(String args[]) throws IOException
{
try
{
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

String result=br.readLine();

if(result.equals("fail"))
throw new UserException();
}
catch (UserException ue)
{
System.out.println(ue.getMessage());
}
}
}

*/
