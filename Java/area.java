import java.util.*;

class area {
	static double area;
	static double areaRect(double wide, double l){
		area = (2*wide*l);
		return area;
	}
		
	public static void main(String[] args){
	
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter how wide it is ?");
	double wide = sc.nextDouble();
	System.out.println("Enter how long it is ?");
	double l = sc.nextDouble();

	double result = areaRect(wide, l);	
	System.out.println("Area of the given paramters is"+ result);
	}
}
