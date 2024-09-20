class wrapper{

	 public static void main(String []args){
		String year = "2024";
		Integer i1 = 22 ;
		//Integer i1 = new Integer(234);
		int yr = Integer.parseInt(year);
		yr++;
		yr+=10;
		
		i1 = Integer.parseInt(year);
		i1++;
		System.out.println(yr);
		System.out.println(i1);


/*

Notes :

wrapper class has super classes too

Numbers is a SUper class for 
	byte,int, short double, long, float

Boolean is a super class

Wrapper classes can access both methods of objects and Numbers


*/
	}
}
