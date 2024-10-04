interface Shape{

		void area(int l, int b);
		void circumference();
		void Display();			
}

class Square implements Shape {
	int a,b;
	double area, cir;
	public void area(int a, int b){
		this.a = a;
		this.b = b;
		area = a*b;
	}
	public void circumference(){
		cir = 2*(a + b);
	}
	public void Display(){
		 System.out.println("The area of the Shape is :"+area);
                 System.out.println("The circumference is :"+cir);	
	}
}

class Rectangle implements Shape {
	int a,b;
	double area, cir;
	public void area(int a, int b){
		this.a = a;
		this.b = b;
		area = 2*(a+b);
	}
	public void circumference(){
		cir = 2*(a+b);
	}
	public void Display(){
	 		System.out.println("The area of the Shape is :"+area);
                        System.out.println("The circumference is :"+cir);	
	}
}	

public class InterShape {
	public static void main(String[] args) {
		Shape sq =  new Square();
		sq.area(2,5);
		//double circm = sq.circumference();
		sq.Display();
	}
}
