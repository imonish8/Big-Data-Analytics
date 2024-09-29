import java.io.*;
public class testInputStream {
	
		public static void main(String[] args)
		throws Exception
		 {

		InputStream input = new FileInputStream("MyFileRead.txt");
		System.out.println(input.available());

		byte [] array = new byte [100];
		input.read(array);
		String data = new String(array);

		System.out.println(data);
		
		input.close();

		}
}
