interface tillGetJob{

	 void pushup();
	 void program();
	 void getIntoTeam();
		
	}

class Monish implements tillGetJob {

		int pushup = 0;
		int program = 0;
		int getIntoTeam = 0;
	
	public void pushup(){
		pushup++;
	}
	public void program(){
		program++;
	}
	public void getIntoTeam(){
		getIntoTeam;
	}
}

public class interface {

		public static void main(String[] args){
		
		tillGetJob t1 = new Monish();
		t1.pushup();
		t1.program();
		t1.getIntoTeam();
		
		System.out.println("Pushup "+pushup++\nProgram "+program+"\ngetIntoTeam "+getIntoTeam);
	}
}
