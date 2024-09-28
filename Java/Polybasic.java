import java.util.*;
class Car{
	double cspeed;
	//boolean cev;
	String chckEV;
	String cname;
	
	Car(){
		
		//created empty super class constructor			
	}
	void Display(){
		// created empty SC Method exits all subclass.
	}
/*
	void isEV(String chckEV){
		// created empty SC Method exits all subclass
		}

*/	
}

class Tesla extends Car{

		
	Tesla(String cname, String chckEV, double cspeed){
		this.cname = cname; //this is input via contructor,  recusrive will explode construnctor do not try.
		this.chckEV = chckEV;
		this.cspeed = cspeed;
		
	}	
	
	void Display(){
		// passing a subclass method to over write the superclass method, must have same name, signature is not important. when over writing or over riding.
		System.out.println("Vehicle is a EV : "+chckEV);
		System.out.println("Vehicle is speed is : "+cspeed);
		System.out.println("Vehcile is Model is : "+cname);
	}	
/*
	//void isEV(boolean cev){
	void isEV(String chckEV){
				
		System.out.println(chckEV);
		// passing value while instanisation.
		this.chckEV = new String(chckEV);
		System.out.println(this.chckEV);
		
	}
*/
}

public class Polybasic {
	
		public static void main(String[] args){

		// Superclass Reference object is not passing or getting the subclass object, why ?	
		Car c1;   
 		//t1  = new Tesla("X Model");
		
		Tesla t1 = new Tesla("X Model", "True", 170.78);
		c1 = t1;
		//c1.isEV("true");
		c1.Display();
		//t1.cev(true);
		//c1.cev(true);
		//c1.Display();

/*
		Car car1;
		Car tesla1 = new Tesla("Tesla X");
		//car1 = tesla1;
		//car1.Display();
		tesla1.isEV("TRUE");
		tesla1.Display();
		
*/		
	}
}
