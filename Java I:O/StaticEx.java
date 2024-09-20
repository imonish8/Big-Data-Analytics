class testEx{
	//static int CODE;
		int CODE;
	//static int codeAssign()
	int codeAssign()
	{
	//CODE = 19;
	CODE++;
	return(CODE);
	}
}

class StaticEx {

	public static void main(String[] args){
	
	testEx s1 = new testEx();
	System.out.println(testEx.codeAssign());
	System.out.println(s1.codeAssign());
	System.out.println(testEx.codeAssign());	
	}
}

