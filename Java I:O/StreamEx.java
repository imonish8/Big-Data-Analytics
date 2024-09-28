import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class StreamEx {
		public static void main(String[] args) {

			try{
	
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
				char c = (char)br.read();
				System.out.println(c);
				String text;
				text = br.ReadLine();
				System.out.println(text);
			}catch (IOException e){
	
				e.printStackTrace();
			}
	}
}
