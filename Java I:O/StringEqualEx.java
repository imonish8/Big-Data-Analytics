public class StringEqualEx{

		public static void main(String[] args){

		String s = "Hell";
		String s1 = "Hello";
		String s2 = "Hello";
		String lowerS2 = "hello";

		boolean b = s1.equals(s1);
		boolean b_lower = s2.equals(lowerS2);

		System.out.println("Checking s1.equals(s1) output");
		System.out.println(b);
		
		System.out.println("Checking s2.equals(b_lower) output");
		System.out.println(b_lower);
		
		
		b = s.equals(s1);
		System.out.println("Checking s.equals(s1) output");
                System.out.println(b);			


			
		}
}
