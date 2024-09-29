class TestWrapper{

		public static void main(String[] args)
		//throws NumberFormatException
		{

		Integer int1 = 100;
		Double double1 = 100.3d;
		Float float1 = 100.24f;
		Character c = 'A';
		Boolean bool1 = true;
		System.out.println(int1+" "+double1+" "+float1+" "+c+" "+bool1);

		Integer int2 = 23;
		int var = 34;
		Integer int3 = var;
		System.out.println("Object created using Integer class "+int2);
		System.out.println("Variable created using integer default object int "+var);
		System.out.println("assignment from variable to object  "+int3);
		
		try{
			int2 = var;
		System.out.println("Printing Object assignment via variable"+ int2);
		}catch(Exception e){
			System.out.println("Failed");
		}
	
		System.out.println();
		String str = new String("303");
		System.out.println("Given string to be processed "+str);
		Integer int4 = Integer.parseInt(str);
		int4 = int4 * 20;
		System.out.println("Parsing String to int(string to int)  :"+ int4);
		Byte bytee = Byte.parseByte(str);
		try{ 	
			System.out.println("String to byte using Wrapper class parseByte() method "+bytee);
		}catch (NumberFormatException e) {

			System.out.println("Trying to parse out of range value to byte");
		}
		
		

	

		
	}
}
