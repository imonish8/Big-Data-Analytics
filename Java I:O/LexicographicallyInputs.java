import java.util.*;
public class LexicographicallyInputs {

    public static void main(String[] args) {
      
        Scanner sc = new Scanner(System.in);
        
        System.out.println("NUmber of Names");
        int n = sc.nextInt();
        
        String names[] = new String[n];
        System.out.println("Give inputs for "+n+" Names");
        for(int i = 0;i < n; i++){
          names[i] = sc.next();
        }
        
        String temp;
        for(int i = 0; i< n; i++){
          for(int j = i + 1; j< n; j++) {
              if(names[i].compareTo(names[j]) > 0 ){
                  temp = names[i];
                  names[i] = names[j];
                  names[j] = temp;
                }
              }
            }
        System.out.println("Alphabaticaly Sorted Array ");
        
        for(int i = 0; i< n; i++) {
          System.out.print(names[i] + " ");
        }
        
        
    }
}
        
        
