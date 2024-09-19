// ALWAYS TAKE INPUT FROM CONSTRUCTOR FOR BEST PRACTICES;
// ALWAYS TAKE INPUT FROM CONSTRUCTOR FOR BEXT PRACTICES;
// ALWAYS TAKE INPUT FROM CONSTRUCTOR FOR BEST PRACTICES;

interface PetrolV{
	String fuelType = "Strictly petrol, cannot change interface variables";

	default void PetrolDisplay(){
		System.out.println(fuelType);
	}		
	public void onPetrol();
	public void Pollution();
	public void Display();
}
interface EV{
	String fuelType = "Strictly Electric, cannot change interface variables";
	
	default void EVDisplay(){
		System.out.println(fuelType);
	}

	public void onElectric();
	public void noPollution();
	public void Display();
}

class anyCar implements PetrolV, EV {

	double speed;
	boolean a;
	boolean d;
	anyCar(){
	}	
	anyCar(double speed, boolean a, boolean d){
		this.speed = speed;
		this.a = a;
		this.d = d;
	}

	public void onPetrol(){
		System.out.println("This is a onPetrol Method whose skeleton is in Interface, over writting / overriiding in interface");
	}
	public void Pollution(){
		System.out.println("This is Petrol Vehicle and it does make Pollution.");
	}
	public void onElectric(){
		System.out.println("This is onElectric Method from EV Interface");
	}
	public void noPollution(){
		System.out.println("This is a Electric vehicle and makes zero carbon emmision.");	
	}
	
	
	public void Display(){
		System.out.println("This is public method from implemented class");
                System.out.println("The speed of any car is :"+speed);
		System.out.println("Pollution : "+a);
		System.out.println("noPollution :"+d);
		
	}
}

public class carInterface{
		public static void main(String[] args){
		
/*
		PetrolV obj1 = new anyCar(22.34d);
		EV obj2 = new anyCar(44.34d);
		anyCar dis = new anyCar();

		//obj2.noPollution(true);
		//obj1.Pollution(true);

		obj1.onPetrol();
		obj2.onElectric();

		dis.noPollution(true);
		dis.Pollution(true);
		dis.Display();
*/
		PetrolV objpetrol = new anyCar(223.33, true, true);
		//objpetrol.Pollution();
		objpetrol.Pollution();
		objpetrol.onPetrol();
		objpetrol.Display();
		
		//objpetrol.onElectric();

		
	}
}
		
			
