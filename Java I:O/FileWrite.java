import java.io.*;
public class FileWrite {
	public static void main(String[] args) {

	try{
		File f1 = new File("MyFileRead.txt");
		FileWriter fw = new FileWriter(f1);
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
