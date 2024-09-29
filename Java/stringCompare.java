public class stringCompare {

		public static void main (String[] args) {

		String firstString = "My name is Hrithik Roshan";
		String secondString = "my name is Rohan";
	
		String smallCase = "my name is monish";
		String bigCase = "My Name is MONISH";

		// simple equal method.

		System.out.println("Checking equal() Method " + firstString.equals(secondString));
		System.out.println("smallCase.equals(bigCase) : "+smallCase.equals(bigCase));
		System.out.println("equals() method is case sensitive");

		System.out.println();
		System.out.println();

		
		String ignoreCaseA =  new String("Hello");
		String ignoreCaseB = new String("hello");

		System.out.println("Checking equalsIgnoreCase() method :"+ ignoreCaseA.equalsIgnoreCase(ignoreCaseB));

	}
}
