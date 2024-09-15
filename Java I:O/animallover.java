import java.util.*;
class animal{
	int age;
	int gender;
	animal(){
		System.out.println("Enter the age of the Pet in Months");
		Scanner sc = new Scanner(System.in);
		
		age = sc.nextInt();
		
		System.out.println("Enter the Gender of the Pet");
		gender = sc.next().charAt(0);
	}
	void Display(){
		System.out.println();
		System.out.println("Pet's Information is here");
		System.out.println();
		System.out.println("Age of the Pet is "+age);
		System.out.println("Gender of the Pet is "+gender);
	}
	
	
}
class dogLover extends animal{
		int num_vac;
		String dog_food;
		
		dogLover(){
			super();
			Scanner sc = new Scanner(System.in);
			System.out.println("Please enter Number of Vaccinations done");
			num_vac = sc.nextInt();
			System.out.println("Please enter Dog's Fav Food");
			dog_food = sc.next();	
		}
		void Display(){
			super.Display();
			System.out.println();
			
			System.out.println("Dog's Food is : "+dog_food);
			System.out.println("Number of Vaccination done are : "+num_vac+" /8");
			System.out.println();

		}
			
	}
class catLover extends animal{
		int num_vac;
		String cat_food;
		Scanner sc = new Scanner(System.in);
		
		catLover(){
			super();

			
			System.out.println("Please enter Number of Vaccinations done");
			num_vac = sc.nextInt();
			System.out.println("Please enter Cat's Fav Food");
			cat_food = sc.next();	
		}
		void Display(){
			super.Display();

			System.out.println();
			System.out.println("Cat's Food is : "+cat_food);
			System.out.println("Number of Vaccination done are : "+num_vac+" /5");
			System.out.println();

		}

			
	}

class horseLover extends animal{
		
		int num_vac;
		String horse_food;
		Scanner sc  = new Scanner(System.in);
		horseLover(){
			super();
			System.out.println("Please enter  Horse/ Foal number of Vaccinations Done so far");
			num_vac = sc.nextInt();
			System.out.println("Please enter Horse/ Foul Favourite Food");
			horse_food = sc.next();
				
		}
		void Display(){
			System.out.println();
			super.Display();
			System.out.println("Number of Vaccinations Done are "+num_vac+" / 13");
			System.out.println("Your Horse/ Foal Favourite Food is "+horse_food);
			System.out.println("Programmer wishes All Pets Happy and Healthy Lifestyle ahead !!! ");
			
		}
	}

public class animallover{
		public static void main(String[] args){
		
		char Likes;
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Please enter Animal of your choice: (eg., Dog = D, Cat = C,Horse = 'H' etc.");
		
		Likes = sc.next().charAt(0);
		
		if( Likes == 'D'){
			dogLover obj1 = new dogLover();
			obj1.Display();
		}else if(Likes == 'C'){
		        catLover obj2 = new catLover();
			obj2.Display();
		}else if(Likes == 'H'){
			horseLover obj3 = new horseLover();
			obj3.Display();	
		}
	}
}
