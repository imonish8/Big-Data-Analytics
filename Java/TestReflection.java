import java.lang.reflect.*;

class UserClass{
	public int a = 133, b = 334,c;
	public UserClass(){
		System.out.println("This is Constructor calling");
	
	}
	public void Method1(int c){
		System.out.println("Method calling of USERcLASS"+c);
			
	}
	public void Method2(){
		System.out.println("Method 2 retrieved in bclass of Class");
	}
}
public class TestReflection {
	public static void main (String[] args)
	throws Exception
	{
		UserClass uobj = new UserClass();
		Class bclass = uobj.getClass();
		

	Constructor[] c1 =bclass.getConstructors();
	for(Constructor c : c1){
		System.out.println(c.getName());
	}
	Method[] m1 = bclass.getMethods();
	for(Method m:m1){
		System.out.println(m.getName());
	}

	//System.out.println(bclass);
	//System.out.println(c1);
	//System.out.println(m1);
	
	Field f1 = bclass.getDeclaredField("a");
	f1.setAccessible(true);
	f1.set(uobj, 100);	
	
	Field f2 = bclass.getDeclaredField("b");
	f2.setAccessible(true);
	f2.set(uobj,200);	
	
	System.out.println(uobj.a);
	System.out.println(uobj.b);	
	
	Method singleMethod =bclass.getMethod("Method1", int.class);	
	singleMethod.invoke(uobj, 220);


	}

}
