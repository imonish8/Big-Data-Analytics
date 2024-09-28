class Outer{
		Outer(){
			data = 1000;
		}		
	int data;
	class Inner {
		public void Display(){
			System.out.println("Inner Class Display"+data);
		}
	}
}

public class ExInner {

	public static void main(String[] args){

		Outer.Inner in = new Outer().new Inner();
		in.Display();	
	}
}
