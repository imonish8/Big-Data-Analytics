class Main implements Cloneable {
	String name;
	int version;
	
	public static void main(String[] args){

	/*	Main Obj1 = new Main();
		Obj1.name = "Java";
		Obj1.version = 21;
		
		System.out.println(Obj1.name);
		System.out.println(Obj1.version);
	
		try {

			Main Obj2 = (Main)Obj1.clone();
			
			System.out.println(Obj2.name);
			System.out.println(Obj2.version);
		}*/
		catch(Exception e){
			
			System.out.println(e);
		}
		Main obj3 = new Main;
		obj3.name = "Python";
		obj3.version = 3;
		
		Main obj4 = obj3;
		System.out.println(obj4);
		System.out.println("Printing Deep Clone now");
		obj3.name = "c";
		
	}
}
