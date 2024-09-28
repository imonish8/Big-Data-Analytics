import java.io.*;
public class FileWrite {
	public static void main(String[] args) {

	try{
		// using class file will open file.
		File f1 = new File("MyFileRead.txt");
		
		// filewriter class writes to file
		FileWriter fw = new FileWriter(f1)

		bufferreader reads from file.;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
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
