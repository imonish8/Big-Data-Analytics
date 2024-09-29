public class StringExample {

	public static void main(String[] args) {

		String s1 = new String("Acts");
		String s2 = s1.concat("JAVA SESSION");
	
		StringBuffer s3 = new StringBuffer("CDAC");
		s3.append("chennai");
		
		StringBuilder s4 = new StringBuilder(s3);
		StringBuilder s5 = s4.reverse();


		System.out.println("Created using String class and concat JAVA SESSION to it"+ s2+ " " + s1);

		System.out.println("Created "+s3 +" using StringBuffer class and appended chennai to it");
		
		System.out.println("Created with StringBuilder "+s4+" and Reversed it using method reverse() "+s5);

	}
}
