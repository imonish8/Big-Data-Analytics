import java.lang.reflect.*;

class PrivateDB{
	private int result;
	/*
	PrivateDB(int result){
		this.result = result;
	}
	*/
	private void setResult(int result){
		this.result = result;
	}

	private boolean getResult(){
		if(result > 50){
			return true;
		}else{
		return false;
		}
	}
}


public class D21_1{
	public static void main(String[] args){

	try{		
	PrivateDB pdb = new PrivateDB();
	
	//cannot access directly
	//pdb.setResult(80);
	//cannot access directly
	//String finalResults = pdb.getResult() + " ";
	//String finalResults = String.valueOf(pdb.getResult());
	//System.out.println("Final result is "+finalResults);
	
	// reflection breaking encapsulation
	Method setResultMethod = PrivateDB.class.getDeclaredMethod("setResult", int.class);
	Method getResultMethod = PrivateDB.class.getDeclaredMethod("getResult");

	setResultMethod.setAccessible(true);
	getResultMethod.setAccessible(true);

	setResultMethod.invoke(pdb,60);
	String finalResults = String.valueOf(getResultMethod.invoke(pdb));
	
	System.out.println("Student Final Result is :"+finalResults);
	

	}catch (Exception e){
		e.printStackTrace();
	}
	
	}	
}
