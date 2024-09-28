import java.util.*;
public class areacircle {
	
	static void CircleInfo(double r){
		double circum = 2*3.14*r;
	 	double area = 3.14*r*r;
		System.out.println("Area and Circumference of the circle are "+area+" "+circum+" respectively");
			
	}
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		double r = sc.nextDouble();
		CircleInfo(r);
	}
}
