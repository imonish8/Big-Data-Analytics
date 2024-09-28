public class DemoWrapper {
	
			public static void main(String[] args){
		
			Integer a = new Integer(12);
			System.out.println("This is Old Value of a");
			System.out.println(b);
			syz(7);
			System.out.println("New Value");
			System.out.println(b);
			
		}
		
		// private, static they are accible when calling in same class
		private static void syz(Integer b){
		
			b = b + 10;
		}

}
