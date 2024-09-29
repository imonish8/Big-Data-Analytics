public class TestBoxing {

	public static void main(String[] args) {

	//primitive to wrapper
	byte a = 1;
	Byte byteObj = new Byte(a);
	
	Integer intObj = new Integer(a);
	Float fltObj = new Float(a);
	byte b1 = byteObj; //wrapper to primitive unboxing automatic.

	try{
	Byte b2 = (Byte) intObj; // explicit because we are mentioning it to jvm explicitly.
	//narrowing conversion which is High range Int to Low range Byte.
	// same goes for Int to Short.
	// Long to Int. Lont to Short. Long to Byte.
	}catch (Exception e){
		System.out.println("Cannot convert Integer Object  into Byte");
	}

	int a1 = 78;
	byte b = (byte)a1;
	//norrowing and explicit conversion.

	Character ch = 'A';
	char a4 = ch;
	
	}
}
