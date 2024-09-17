import java.util.*;
/*
class Supreme1{
	private static int priv1= 1;
	private static int priv2 =2;
	
	void Display3(){
		System.out.println("Private to Supreme1: "+priv1);
		System.out.println("Private to Supreme1: "+priv1);
	
	}
}
*/
class Supreme{
	private static String Suo_Motu;
	private static String Constit_review;

	String hearing_case;
	String Granting_bail;

	private String Level;

	
	Supreme(){
		Suo_Motu = "Power Remains to Supreme court only, This should not be printed on anyther child objects";
		Constit_review = "Power Remains to Supreme Court only, Not accessible to child objects.";
		hearing_case = "All Courts  can hear cases";
		Granting_bail = "All Courts have power to grant Bail";
		Level = "Top Most Court";
		}
	void Display(){

		
			if(this.getClass() == Supreme.class){
                                 System.out.println("Power remains to Supreme Court Only, that is "+Suo_Motu);
                                 System.out.println("Power remains to Supreme Court only, That is "+Constit_review);
				 System.out.println("Unique to this court, that is :"+Level);
                        }
				 System.out.println("Common to all Courts, That is :"+hearing_case);
				 System.out.println("Common to all Courts, that is :"+Granting_bail);
		
		
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
			System.out.println("High Court Power");
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
			System.out.println("District Power");
			System.out.println("Unique Level of this court, That is,"+Level);
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
			System.out.println("Subordinate Powers");
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
			System.out.println("Specialized And tribunal Powers");
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

		//Supreme obj1 = new Supreme();
		//obj1.Display1();
	
		//High obj2 = new High();
		//obj2.Display();
	
		//Subordinate obj3 = new Subordinate();
		//obj3.Display();
	
		//District obj4 - new District();
		//obj4.Display();

		//SpecializedTribunal obj5 = new SpecializedTribunal();
		//obj5.Display();
	
		People obj6 = new People();
		//obj6.Display();
		obj6.Display();

		//Supreme.Display1();
		
		//Supreme1 s1 = new Supreme1();
		//s1.Display3();
	}		
}
