public class GenricClass<varOne, varTwo> {
	private varOne objOne;
	private varTwo objTwo;

	public GenricClass(varOne objOne, varTwo objTwo){
		this.objOne = objOne;
		this.objTwo = objTwo;
	}

	public void methodA(varOne obj1, varTwo obj2){
		this.objOne = obj1;
		this.objTwo = obj2;
	}

	public void methodB(){
		System.out.println("Value of Object One (varOne): "+objOne);
		System.out.println("Value of Object two (varTwo): "+objTwo);
	
	}


	public static void main(String[] args){

		GenricClass<Integer, String> gc1 = new GenricClass<>(04, "Big Data Monish");
		System.out.println("Before Manipulation :");
		gc1.methodB();

		gc1.methodA(9999,"Nule Big Data");
		System.out.println("After Manipulation :");
		gc1.methodB();	
	}
}
