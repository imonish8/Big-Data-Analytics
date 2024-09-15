public class factorial {
		int n;
		factorial(int n){
			if(n == 1){
			 return 1;
			}
			else{
				return(n*factorial(n-1));
			}
		}
		void Display(){
		int result = n*factorial(n-1);
		System.out.println("Factorial is"+result);
		}
		public static void main(String[] args){

			factorial fact = new factorial(7);
			fact.Display();
		}
}
