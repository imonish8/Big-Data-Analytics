import java.io.*;
public class FileWrite {
	public static void main(String[] args) {

	try{
<<<<<<< HEAD:Java/FileWrite.java
		// using class file will open file.
		File f1 = new File("MyFileRead.txt");
		
		// filewriter class writes to file
		FileWriter fw = new FileWriter(f1)

		bufferreader reads from file.;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
=======
		File f1 = new File("MyFileRead.txt");
		FileWriter fw = new FileWriter(f1);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
>>>>>>> 4bff3f2 (FILE HANDLING):Java I:O/FileWrite.java
		String str;
		while(true){
			str = br.readLine();
			if(str.equals("EOF"))
			break;
			fw.write(str+ "\n");
		
		}
		br.close();
	}catch(IOException e){
		e.printStackTrace();
	}
}
}
