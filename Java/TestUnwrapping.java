public class TestUnwrapping {
      public static void main (String[] args) {
      
          Integer a = 33;
          int i = a.intValue();
          int j = a;
          // object assigning to variable > unwrapping
          // variable is being assigned to object > wrapping.
          System.out.println("Done via Internally "+j);
          System.out.println("Unwrapping done Explicitly"+i);
      }
      
}
