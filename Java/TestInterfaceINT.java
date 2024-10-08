public class TestInterfaceINT{
	public static void main(String[] args){

	Arithmetic arth = new Arithmetic();
	int number = 5;
	System.out.println("Square of "+number+" is " +arth.square(number));

	}
}


interface Test{
	int square(int n);
}
class Arithmetic implements Test{

	public int square(int n){
	return n*n;
	}
}
