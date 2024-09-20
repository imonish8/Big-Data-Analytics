interface coffeeMug{

	char coffee = 'C';
	
	void haveCoffee(){
	}
	void haveMuffin(){
	}
}

interface teaMug{
	char tea = 'T';
	
	// by conventions interface have static variable field
	// by conventions interface are full abstraction of subclasses and public.


	void haveTea(){
	}
	void haveBiscuit(){
	}
}

class guests implements coffeeMug, TeaMug{
		
		char choice;
		char biscuits;
		guests(){
			System.out.println("Hello Guests, What would you like to have C or T ? ");
			choice = sc.next.charAt(0);
	
			switch(choice){
				case 'T' :
					System.out.println("Great Choice guests, i'll bring Tea, What would you like to have with tea, Biscuits ?")
					biscuits = sc.next().charAt(0);
						if(biscuits == 'Y'){
							System.out.println("Bringing Tea with Buiscuits ");
						}else{
							System.out.println("I'll Bring Tea ");
						}
				break;
				case 'C' :
					System.out.println("Great choice, i'll Bring Coffee, what would you like to have with coffee, muffins ?");
					muffins = sc.next().charAt(0);
						if(muffins == 'Y'){
							System.out.println("Bringing Coffee and Muffins ");
						}else{
							System.out.println("Bringing Coffee ");
						}
				break;
				Default :
					System.out.println("Wrong House");
				
			}
			System.out.println("Thank you for visiting, have a safe home back ");
		
		}	
	}
