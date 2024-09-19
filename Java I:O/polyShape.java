import java.util.*;
interface Shape
{
	static double PI=3.14d;
	//double area = 1.0d;
	//double circumference= 1.0d;

		void area();
		void circumference();
		
		/*
		void display()
		{
		System.out.println("Area is "+area);
		System.out.println("Circumference is "+circumference);
		}
		*/
		void Display();
		}

class Circle implements Shape
	{
		float radius;
		double area;
		double circumference;
		Circle(float radius)
	{
		this.radius=radius;
	}
	public void area()
	{
		area=PI*radius*radius;
	}

	public void circumference()
	{
	circumference=2*PI*radius;
	}
	public void Display(){
		System.out.println("Area of the Circle is "+area);
		System.out.println("Circumference of the circle is "+circumference);
	}
	}

class Rectangle implements Shape

	{
		float length,breadth;
		double area;
		double circumference;
	Rectangle(float length,float breadth)
	{
		this.length=length;
		this.breadth=breadth;
	}
	public void area()
	{
	area=length*breadth;
	}
	public void circumference()
	{
	circumference=2*(length+breadth);
	}
	public void Display(){
                System.out.println("Area of the Rectangle is "+area);
                System.out.println("Circumference of the Rectangle is "+circumference);
        }
	
	}

	class Square implements Shape
	{
	float side;
	double area;
	double circumference;
	Square(float side)
	{
		this.side=side;
	}
	public void area()
	{
	area=side*side;
	}
	public void circumference()
	{
	circumference=4*side;
	}
	public void Display(){
                System.out.println("Area of the Square is "+area);
                System.out.println("Circumference of the Square is "+circumference);
        }
	}

class polyshape
{
	public static void main(String args[])
	{
	Scanner sc=new Scanner(System.in);
	System.out.println("Enter the Shape (1 for Circle,2 for Rectangle, 3 for Square");
	int choice;
	choice=sc.nextInt();

	Shape s=null;


	switch(choice)
		{
		case 1:
		System.out.println("Enter the radius of the circle");
		float radius=sc.nextFloat();
		Circle c1=new Circle(radius);
		s=c1;

		//s=new Circle(radius);
		break;

		case 2:
		System.out.println("Enter the length and breadth  of the rectangle");
		float length=sc.nextFloat();
		float breadth=sc.nextFloat();
		Rectangle r1=new Rectangle(length,breadth);
		s=r1;

		//s=new Rectange(length,breadth);
		break;

		case 3:
		System.out.println("Enter the Side of the square");
		float side=sc.nextFloat();
		Square s2=new Square(side);
		s=s2;

		//s=new Square(side);
		break;

		default:
		System.out.println("Invalid input");
		}


		s.area();
		s.circumference();
		s.Display();


	}	
}
