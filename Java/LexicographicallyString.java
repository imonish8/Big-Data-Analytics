public class LexicographicallyString {
  
  public static void main(String[] args) {
  
    int n = 4;
    String names[] = {"Arjun", "Apple", "Banana", "Coconut"};
    String temp;
    for(int i =0; i< n; i++){
      for(int j = i + 1; j < n; j++) {
        if(names[i].compareTo(names[j]) > 0){
            temp = names[i];
            names[i] = names[j];
            names[j] = temp;
            }
          }
          
        }
        
        
        
        System.out.println("The names in alphabatically Order are: ");
        for(int i = 0;i < n; i++){
          System.out.println(names[i]);
          }
       
       
       
       
  }
}
