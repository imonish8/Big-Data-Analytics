import java.util.*;
import java.io.*;

public class D17_1{
	public static void main(String[] args){

		Scanner sc =  new Scanner(System.in);
		System.out.println("Please enter String, appending to FILE");
		String ustr = sc.next();
		System.out.println("Please enter Integer, to append to FILE");
		int uint = sc.nextInt();

		try{

			FileWriter writerObj = new FileWriter("output.txt");
			writerObj.write("Integer "+uint+"\n");
			writerObj.write("String "+ustr+"\n");
			
			writerObj.close();
		}catch (IOException e){
			
			System.out.println("Error occured, please chk code");
			e.printStackTrace();
		}finally{
			sc.close();
		}

	}
}
