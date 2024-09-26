class Anonymous {
		public void Display(){
			System.out.println("Anonymous Class");
		}
	}

class testAnonymous{

	 static Anonymous a1 = new Anonymous() {
		
		public void Display(){
		super.Display();
		System.out.println("Overriden Method Display anonymous inner class");
	
		}

	};
	static Anonymous a2 = new Anonymous() {
		public void Display(){
		super.Display();
		System.out.println("Overriden method by objext/class a2");
		}
	};
	public static void main(String[] args){
		
	a1.Display();
	a2.Display();	
	}
}



//used for Single handled cases.

