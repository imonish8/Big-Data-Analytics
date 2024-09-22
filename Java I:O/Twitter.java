import java.io.*;

public class Twitter {
		
			public static void main(String[] args){
				String url = "https://x.com/__mn8_";
				
				String[] cmd = {"open", "-a", "Safari", url};
				try{
					Runtime.getRuntime().exec(cmd);
					System.out.println("Twitter Opening @__mn8_, Enjoy Surfring");
					
				} catch (IOException e) {
				System.out.println("@Monish : https://x.com/__mn8_ ");
				System.out.println("Runtime error, Open Yourself");
				e.printStackTrace();
				}
		}
}
