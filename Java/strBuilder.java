class strBuilder{

		public static void main(String[] args){
	
//methods in class = capacity, replace, reverse, insert, ensurecapacity

		StringBuilder str1 = new StringBuilder("Hello");
		System.out.println(str1);
		str1.append("jAVA");
		System.out.println(str1);			
		
		//insert
		System.out.println("String Insertion Demo \n");
		str1.insert(2,123);
		System.out.println(str1);
		System.out.println();
	
		System.out.println("String Reverse Demo \n");
		str1.reverse();
		System.out.println(str1);
		System.out.println();
	
		System.out.println("String Replace takes two params - (index_start,index_end, NEWelement)");
		str1.replace(2,8, "I love java");
		System.out.println(str1);
		System.out.println();
	
		System.out.println("Capacity() returns current capacity of str1");
		System.out.println(str1.capacity());
		System.out.println();
	
		System.out.println("ensurecapacity() returns minimum of str2 empty");
		StringBuilder str2 = new StringBuilder();
		System.out.println("Initial Capacity using capacity()"+str2.capacity());
		str2.ensureCapacity(30);
		System.out.println("after using ensureCapacity() "+ str2.capacity());
		
	}
}
