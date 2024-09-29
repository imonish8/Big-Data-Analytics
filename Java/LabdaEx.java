// @functionalProgramming

interface student {
	
	public int  useID(int yes);
}

public class LabdaEx {

	public static void main(String[] args) {
	

	student obj2 = (yes) ->	{ 
	yes = 1;
	System.out.println("Student has bought the ID "+yes);
	return yes;
	};
	System.out.println(obj2.useID(1));
	


	
	student obj3 = (no) -> {
	no = 0;
	System.out.println("Student has not bought the ID "+no);
	return no;
	};
	System.out.println(obj3.useID(0));
	


	}

}
