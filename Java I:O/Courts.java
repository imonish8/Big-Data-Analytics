// Under Consistitution we have 5 courts and 2 Subordinate Courts

class Supreme{
	private String Suo_Motu;
	private String Constitutional_review;

	String hearing_case;
	String Granting_bail;

	private String Level;

	Supreme(){
		Suo_Motu = "The Supreme Court can take up matters on its own (suo motu) without anyone formally filing a case";
		Constitutional_review = "The Supreme Court only has power to Reject / Accept Laws Passed in parliment";
		hearing_case = "All Courts court can hear cases";
		Granting_bail = "All Courts have power to grant Bail";
		Level = "Top Most Court";
		}
	void Display(){
		System.out.println("Private to/ Power remains to Supreme Court Only, that is "+Suo_Motu);
		System.out.println("Private to/ Power remains to Supreme Court only, That is "+Constitutional_review);
		System.out.println("Common to all Courts, That is :"+hearing_case);
		System.out.println("Common to all Courts, that is :"+Granting_bail);
		System.out.println("Unique to each court, that is :"+Level);
		
		}
	 
	}

class High extends Supreme{
	//state
	String Level;

	High(){
		super();
		Level = "State Level";
		}
	void Display(){
		super.Display();
		System.out.println("Unique to High Court, that is, "+Level);
		
		}
		
	}

class District extends Supreme {
		String Level ;
		District(){
			super();
			Level = "District Level";
		}
		void Display(){
			super.Display();
			System.out.println("District Courts hold a Title which is Unique, That is,"+Level);
		}
	}

class Subordinate  extends Supreme{
		String Level;
		Subordinate(){
			super();
			Level = "Civil Criminal Level";
			
		}	
		void Display(){
			super.Display();
			System.out.println("Subordinate hold a unique Title, that is "+Level);
		}	
	}

class SpecializedTribunal extends Supreme{
		
		String Level;
		SpecializedTribunal(){
			super();
			Level = "Family Level";
		
		}
		
		void Display(){
			super.Display();
			System.out.println("Specialized Tribunal Court Hold such a Power "+Level);
		}
	}
class People extends Supreme{

		String Level;
		People(){

			super();
			Level = "People Resolution";
		}
		void Display(){
			super.Display();
			System.out.println("People level Court Conducts and Executes "+Level);
		}
	}
public class Courts {
		public static void main(String[] args){

	//	Supreme obj1 = new Supreme();
	//	obj1.Display();
	
		High obj2 = new High();
		obj2.Display();
	/*	
		Subordinate obj3 = new Subordinate();
		obj3.Display();
	
		District obj4 - new District();
		obj4.Display();

		SpecializedTribunal obj5 = new SpecializedTribunal();
		obj5.Display();
	
		People obj6 = new People();
		obj6.Display();
	*/
	}		
}
