import java.io.*;

public class meditate {

		public static void main(String[] args){
			String url = "https://www.youtube.com/watch?v=BWMcR35D-cE";
			String[] cmd = {"open", "-a", "Safari", url};
			try {
				Runtime.getRuntime().exec(cmd);
				System.out.println("Hey Monish, Meditation beings in 3, 2, 1 ....");
			}catch (IOException e) {
				System.out.println("Meditation URL : https://www.youtube.com/watch?v=BWMcR35D-cE");
				e.printStackTrace();
			}
		}
}
