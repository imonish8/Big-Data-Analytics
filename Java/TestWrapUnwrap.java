public class TestWrapUnwrap {

    public static void main(String[] args) {
    
        char ch = 'A';
        Character chrobj = ch;
        //wrapping ch variable type value in wrapper class Character.
        
        Byte a = 10;
        Byte byteObj = a; //wrapping byte data into byte object
        
        int b = 10;
        Integer intObj = b;// wrapping int data into Integer Obj
        float c = 10.33f;
        Float fltObj = c;
        
        double dbl = 12992.22d;
        Double dbObj = dbl;
        
        System.out.println();
        System.out.println("Display values of Wrapper class object ");
        System.out.println("Character : "+chrobj);
        System.out.println("Byte :"+byteObj);
        System.out.println("Integer :"+intObj);
        System.out.println("FLoat :"+fltObj);
        System.out.println("Double :"+dbObj);
        System.out.println("Assigning VAriable type to object type");
        
        System.out.println();
        char ch1 = chrobj;
        byte aa = byteObj;
        int bb = intObj;
        float cc = fltObj;
        double dd = dbObj;
        
        System.out.println("Retrieving Object values again in new VAriable of respective data type");
        
        System.out.println("char type: "+ch1);
        System.out.println("byte type: "+aa);
        System.out.println("int type :"+bb);
        System.out.println("float type :"+cc);
        System.out.println("double type :"+dd);
        System.out.println();
        
        
        }
}
