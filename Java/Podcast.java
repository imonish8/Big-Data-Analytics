import java.io.*;
public class Podcast {

		public static void main(String[] args){
			String url = "https://podcasts.apple.com/in/podcast/the-strangest-secret-by-earl-nightingale/id1516658885";
			String cmd [] = {"open", "-a", "Safari", url};
			try{
				Runtime.getRuntime().exec(cmd);
				System.out.println("Podcast is running");
				
			} catch (IOException e) {
			
			System.out.println("Listen here :"+url);
			e.printStackTrace();
			
			}
		}
}
