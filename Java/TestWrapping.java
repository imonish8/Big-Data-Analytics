public class TestWrapping {
       public static void main (String[] args) {
       
          int a = 20;
          
          Integer i = Integer.valueOf(a);
          Integer j = a;
          
          System.out.println("Here printing value of int ");
          System.out.println("Here printing value of Integer Object i "+i);
          System.out.println("Here printing Value of Integer j "+j);
        }
}
