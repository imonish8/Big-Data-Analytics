import java.io.*;
public class meetJava{

		public static void main(String[] args){

			String url = "https://meet.google.com/dow-tqkk-ayg";
			String cmd[] = {"open", "-a","Safari", url};
			try{
				Runtime.getRuntime().exec(cmd);
				System.out.println("Opening Java Meet : https://meet.google.com/dow-tqkk-ayg");
			}catch (IOException e){
				System.out.println("Runtime error, Please copy https://x.com/__mn8_ in Safari yourself.");
				e.printStackTrace();
			}
	}
}
