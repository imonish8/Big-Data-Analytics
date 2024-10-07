
import java.io.*;
import java.io.RandomAccessFile.*;

public class D18_1 {
	public static void main(String[] args){
	try{
	RandomAccessFile raf = new RandomAccessFile("output.txt", "rw");
	
	raf.writeInt(12344);
	raf.writeDouble(1124.23d);
	raf.writeUTF("I Love Java");
	
	raf.seek(1);
		
	String msg = raf.readUTF();
	int num = raf.readInt();
	double db = raf.readDouble();
	
	System.out.println("String from File :"+msg);
	System.out.println("Integer from file :"+num);
	System.out.println("Double from file :"+db);

	raf.close();
	}catch (IOException e) {

		System.out.println("Error occured");
		e.printStackTrace();
	}finally{
		System.out.println("Finally Program run successfully");
	}
	}
}	
