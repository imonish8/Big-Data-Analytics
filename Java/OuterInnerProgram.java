public class OuterInnerProgram{
	void Display(){
		System.out.println("This is the Outer class Display Method.");
	}

	class Inner {
		void Display(){		
		System.out.println("This is the Inner class Display method");
		}
	}

	public static void main(String[] args){
		
		OuterInnerProgram  oin = new OuterInnerProgram();
		OuterInnerProgram.Inner inner = oin.new Inner();
	
		oin.Display();
		inner.Display();
	}
}
