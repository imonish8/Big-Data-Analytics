public class MethodX{
		static void display(){
			System.out.println("Static Display method");
		}
		static void add(int arg1, float arg2){
		float arg3= arg1 + arg2;
		System.out.println("Inside the method printing "+ arg3);
		
		}
		static int fact(int n){
			int fact =1;
			for(int i=1;i<=n;i++)
			fact*=i;
		return fact;
		}

		public static void main(String[] args){
		
			MethodX.display();
			MethodX.add(2,3.2f);
			int factorial = fact(3);
			System.out.println("Factorial is: "+factorial);

		}
}
