public class matrixAdd {

	public static void main(String[] args){
		
		int a[][] = {{1,3,4},{2,5,3}, {2,55,1}};
		int b[][] = {{22,43,53},{24,66,73},{21,22,75}};
	
		int c[][] = new int[3][3];

		for(int i = 0; i< 3; i++){
			for(int j = 0;j<3;j++){
				c[i][j] = a[i][j] + b[i][j];
				System.out.print(c[i][j]+" ");
				}
			System.out.println();
			}
	}
}
