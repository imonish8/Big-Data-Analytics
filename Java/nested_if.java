public class nested_if{
		public static void main(String[] args){
			int a = 2;
			int b = 200;
			int c = 233;
			int d = 344;
			
			if(b>a){
				if(b>c){
					System.out.println("B is greater than 'a' but not greater than 'c'");
					}
				if(d>c){
					System.out.println("C is greater than 'b' but not greater than 'd'");

					}	
			}else{
				System.out.println("This was the example of Nested if else, here it ends");

			}
                }
}
