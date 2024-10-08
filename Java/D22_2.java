interface Student{

	void Marks(int total);	

}


public class D22_2{
	public static void main(String[] args){
	Student d1 = (total) -> {
	
		System.out.println("Abstract Method calling using Lambda");
		System.out.println("Total Marks for student is :"+total);
	
	};
	
	d1.Marks(80);

	}	
}
