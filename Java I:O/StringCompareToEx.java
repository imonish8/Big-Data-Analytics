public class StringCompareToEx{

			public static void main(String[] args){

			String s1 = "Abhi";
			String s2 = "Viraaj";
			String s3 = "Abhi";
			int a = s1.compareTo(s2);
			System.out.println("CHECKING COMPARE TO WITH OUTPUT INT");
			System.out.println(a);
			
			System.out.println("demo when same same");
			a = s1.compareTo(s3);
			System.out.println(a);

			System.out.println("when string one is greater in length");
			a = s2.compareTo(s1);
			System.out.println(a);		
			}
}
