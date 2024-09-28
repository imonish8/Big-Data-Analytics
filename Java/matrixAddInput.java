import java.util.*;
public class matrixAddInput{
	public int MatrixA[][];	
	int m,n;
	public void inputMatrixA(){
		System.out.println("Enter Length");
		Scanner sc = new Scanner(System.in);
		m = sc.nextInt();
		System.out.println("Enter width");
		n = sc.nextInt();
		
		int MatrixA[][] = new int[m][n];
		System.out.println("Enter values for Matrix now...");
		
			for(int i =0; i<m; i++){
				for(int j =0;j<n;j++){
				System.out.println("enter value for position "+i+" "+j);
				MatrixA[i][j] = sc.nextInt();
				this.MatrixA = MatrixA;
				}
			}
	}
	public void printMatrix(){
		for(int i =0; i<m;i++){
			for(int j=0;j<n;j++){
				System.out.print(MatrixA[i][j] +" ");
			}
		}
	}

	public static void main(String[] args){
		
		matrixAddInput m1 = new matrixAddInput();
		
		m1.inputMatrixA();
		
		System.out.println("Matrix is here ");
	
		m1.printMatrix();
		
	}
}	
	
		

		
