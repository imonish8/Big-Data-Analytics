import java.util.*;
class Shape
{
	double area;
	double PI = 3.14;
	
	public void area(){
		
			
	}
	public void circumference(){

	}
	public void Display(){
	
	}
}

class Circle extends Shape {
		double radius;

		Circle(double radius){
		//Scanner sc = new Scanner(System.in);
		//System.out.println("Enter the radius of circle");
		this.radius = radius;
		}
		
		public void area(){
		area = PI*radius*radius;
		
		}
		public void circumference(){
		circumference = 2*PI*radius;	
		}
}	
class Rectangle extends Shape 
  		{

		double length;
		double width;
		
		Rectangle(){
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter The Length of Rectangle");
			length = sc.nextDouble();
			System.out.println("Enter the width of Rectangle");
			width = sc.nextDouble();
			}
			public void area(){
				area = length*width;
				
			}
			public void circumference(){
				circumference = 2*(length+width);
			}
			
		}
class Quadrilateral extends Rectangle{
			//
		}
		
class Triangle extends Shape {
			double breadth;
			double height;
			
			Triangle(){
				Scanner sc = new Scanner(System.in);
				System.out.println("Enter a breadth of triangle");
				breadth = sc.nextDouble();
				System.out.println("Enter the width of triangle");
				height = sc.nextDouble();
			}
			public void area()
			{
			area = 0.5*breadth*height;
			

			}
		
	}
public class Polymorphism{

			public static void main(String[] args){
			Shape s = new Shape();
			
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter Your choice (1. for Circle, 2 For Rectangle, 3 For traingle");
			int choice = sc.nextInt();
			switch(choice){
				case 1 :
					Circle c = new Circle();
					s = c;
				break;
				case 2 :
					Rectangle r = new Rectangle();
					s = r;
				break;
				case 3 :
					Triangle t = new Triangle();
					s = t;
				break;
				default:
					System.out.println("Invalid Input");
				}
				
			double areaOutput = s.area();
			System.out.println("Area of the Shape is "+ areaOutput);
			System.out.println("Area of the Shape is "+s.area());
		}
}
			


