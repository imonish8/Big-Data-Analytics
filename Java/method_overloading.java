public class method_overloading{
		public static void main(String[] args){
			// loading the methods.
			int ans = methodA(100,200);
			int ans1 = methodA(100,200,300);
			System.out.println(ans);
			System.out.println(ans1);
			System.out.println(methodA("2000",'V'));
		}
		
		static int methodA(int a,int b){
			//return type
			int temp;
			temp = a + b;
			System.out.println("Inside First Method");
			return temp;
		}
		static int methodA(int a, int b, int c){
			System.out.println("\n Inside 2nd Method");
			return(a+b+c);
			
		}
		static String methodA(String a, char c){
			System.out.println("\n Inside Third method");
			String s = a+c;
			return s;
		}
		
}
