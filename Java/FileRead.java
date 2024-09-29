import java.io.*;
public class FileRead {
	public static void main(String args []){
	try{

	File f1 = new File("MyFileRead.txt");
	BufferedWriter br = new BufferedWriter(new FileWriter(f1));
	BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));

	String str;
	//while((str = br1.readLine()) != null)
	//{
		str = br1.readLine();
		br.write(str);
	//}
	br.close();

	}catch(IOException e){	
	e.printStackTrace();
	}
	
}
}
