public class StringEqOperatorEx{

			public static void main(String[] args){

				String s1 = "Java";
				String s2 = "Java";
				String String_Object = new String("Java");
				boolean b = (s1 ==s2);
				System.out.println(b);
				
				System.out.println("Comparing with String_Object JAVA");
				b = (s1 == String_Object);
				System.out.println(b);
		}
}
