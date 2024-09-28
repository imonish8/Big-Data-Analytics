import java.util.*;
public class matrixAddInputs {

	public static void main(String[] args) {
	
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter Dimensions M x N for 1st MAtrix");
	int m = sc.nextInt();
	int n = sc.nextInt();
	
	System.out.println("Enter K and L DImensions for second matrix");
	int K = sc.nextInt();
	int L = sc.nextInt();
	
	int darr[][] = new int[m][n];
	int darr2[][] = new int[K][L];
	
	System.out.println("Enter values for 2st MAxtrix");
	for(int i = 0; i < m ;i++){
		for(int j = 0; j<n; j++) {
		  darr[i][j] = sc.nextInt();
		  }
	}
	
	
	System.out.println("Enter Values for 2nd MAtrix");
	for(int i = 0; i< K; i++) {
		for(int j = 0; j<L ;j++) {
		 	darr2[i][j] = sc.nextInt();
		 	
		}
	}
	
	System.out.println("Both Matrix VAlues are taken, Processing for further addition");
	
	int c[][] = new int[m][L];
	
	for(int i = 0; i< m ; i++) {
		for( int j = 0; j< L ; j++) {
			c[i][j] = darr[i][j] + darr2[i][j];
			
		}
	}

	System.out.println("The 2D Array Addition is below :");
	
	for(int i=0 ; i<m ; i++ ) {
		for(int j =0; j< L ; j++ ) {
		
			System.out.print(c[i][j] + " ");
		}
	System.out.println();
	}
	
}
}
