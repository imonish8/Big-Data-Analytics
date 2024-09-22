// static variables recall their previous value even if new object is called of the same class.
// static variables can only be updated using object of that class n class itself.


public class StaticObject {
			//int code;
			static int code = 10;

			//StaticObject(){
				code++;
			//}
		public static void main(String args[]){
			
			//int code = 0;
			StaticObject s1 = new StaticObject();
			StaticObject s2 = new StaticObject();
			StaticObject s3 = new StaticObject();
		
			System.out.println(code);
System.out.println(s2.code);
System.out.println(s3.code);
		}
}
