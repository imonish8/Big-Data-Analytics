public class factorial {
		int n;
		int res;
		factorial(int n){
			if(n == 1){
			 return 1;
			}
			else{
				 res = (n*factorial(n-1));
			}
		}
	
		void Display(){
			System.out.println("Factorial is"+res);
		}
	


		public static void main(String[] args){

			factorial fact = new factorial(7);
			fact.Display();
		}
}
