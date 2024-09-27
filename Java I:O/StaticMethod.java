class StaticMethod2 {
    static int square(int y) {
      return y*y;
      }
  }
// static can be called using OBject or Class itself.
// ealier versions werent allowing object to call static.
//those privalages were only to CLass.
public class StaticMethod {

    static int cube (int x) {
        return x*x*x;
        }
    public static void main(String[] args) {
      
      StaticMethod2 obj = new StaticMethod2();
      int res2 = obj.square(2);
      System.out.println(res2);
      
      StaticMethod obj_1 = new StaticMethod();
      
      int res = StaticMethod.cube(5);
      int res_ = obj_1.cube(2);
      System.out.println(res_);
      System.out.println(res);
      }
  }
