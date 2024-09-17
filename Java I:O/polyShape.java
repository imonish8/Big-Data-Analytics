import java.util.*;
class Shape
{
	static double PI=3.14d;
	double area;
	double circumference;

		void area()
	{
	}
		void circumference()
		{
		}
		void display()
		{
		System.out.println("Area is "+area);
		System.out.println("Circumference is "+circumference);
		}
		}

class Circle extends Shape
	{
		float radius;
		Circle(float radius)
	{
		this.radius=radius;
	}
	void area()
	{
		area=PI*radius*radius;
	}

	void circumference()
	{
	circumference=2*PI*radius;
	}
	}

class Rectangle extends Shape
	{
		float length,breadth;
	Rectangle(float length,float breadth)
	{
		this.length=length;
		this.breadth=breadth;
	}
	void area()
	{
	area=length*breadth;
	}
	void circumference()
	{
	circumference=2*(length+breadth);
	}
	}

	class Square extends Shape
	{
	float side;
	Square(float side)
	{
		this.side=side;
	}
	void area()
	{
	area=side*side;
	}
	void circumference()
	{
	circumference=4*side;
	}
	}

class polyShape
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
		s.display();


	}	
}
