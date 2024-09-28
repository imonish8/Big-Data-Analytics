 class Student {
  
    int rollno;
    String name;
    String city;
    
    Student(int rollno, String name, String city){
      this.rollno = rollno;
      this.name = name;
      this.city = city;
    }
    
    
    
    public String toString() {
      return rollno+" "+name+" "+city;
    }
 
 }
 public class ToStringEx{
        public static void main(String args[]) {
        Student s1 = new Student(101, "Raj", "Lucknow");
        Student s2 = new Student(102, "Rajesh", "Delhi");
        
        System.out.println(s1.toString());
        System.out.println(s2);
        }
}


