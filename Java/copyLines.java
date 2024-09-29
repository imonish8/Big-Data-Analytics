import java.io.FileReader;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.IOException;

public class copyLines {
	public static void main(String[] args){

		BufferedReader inputStream = null;
		PrintWriter outputStrean = null;

		try {

		inputStream = new BufferedReader(new FileReader("MyFileRead.txt"));
		outputStream = new PrintWriter(new FileWriter("MyFileRead.txt"));
		
		String l;
		
		while((l = inputStream.readLine()) != null) {

			outputStream.println();
		}
	}finally {
		
		if(inputStream != null){
			inputStream.close();
		}
		if(outputStream != null){

			outputStream.close();

		}
	}

	
}
}
