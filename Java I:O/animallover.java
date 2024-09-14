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

			
	}

public class animallover{
		public static void main(String[] args){
		
		int Likes;
		Scanner sc = new Scanner(System.in);
		System.out.println("Please enter Animal of your choice: (eg., Dog = 0, Cat = 1, etc.");
		Likes = sc.nextInt();
		if( Likes == 0){
			dogLover obj1 = new dogLover();
			obj1.Display();
		}else{
		        catLover obj2 = new catLover();
			//obj2.catLover();
		}
	}
}
