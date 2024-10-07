public class TestGeneric<varOne, varTwo> {
	private varOne objOne;
	private varTwo objTwo;
	
	public TestGeneric(varOne objOne, varTwo objTwo){
		this.objOne = objOne;
		this.objTwo = objTwo;

	}

	public void methodA(varOne obj1, varTwo obj2){
		this.objOne = obj1;
		this.objTwo = obj2;

	}

	public void methodB(){
		System.out.println("Value of Object 1 (varOne) : "+objOne);
		System.out.println("Value of Object 2 (varTwo) : "+objTwo);
	}
	public static void main(String [] args){
		
		TestGeneric<Integer, String> gc1 = new TestGeneric<>(100, "BigData");
		System.out.println("Before Manipulation :");
		gc1.methodB();
		System.out.println();
		System.out.println("After manipulation");
		gc1.methodA(9999, "Universe");
		gc1.methodB();
	}
}
