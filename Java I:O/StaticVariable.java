public class StaticVariable {

    static int count = 0;
    StaticVariable() {
    
        count++;
        System.out.println(count);
        }
  
  public static void main(String args[]) {
    
      StaticVariable obj = new StaticVariable();
      StaticVariable obj1 = new StaticVariable();
      StaticVariable obj2 = new StaticVariable();
    }
}
      
