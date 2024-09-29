import java.util.*;
public class StringTokenizer1 {
	public static void main(String[] args) {

		String str = "This is testing of Tokenizer";

		StringTokenizer st = new StringTokenizer(str, ",");

		while (st.hasMoreTokens()){
			System.out.println(st.nextToken());
		}
	}
}
