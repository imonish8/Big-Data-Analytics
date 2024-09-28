import java.util.*;
class primeNum{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter A number");
		int n = sc.nextInt();
		int m,flag;
		for( n = 2; n<=100; n++){
			flag = 0;
			m = n/2;
			for(int i = 2;i<=m;i++){
				if(n%i == 0){
				flag =1;
				break;
				}
			}
		if(flag == 0){
			System.out.println(n+" IS A prime Number");
		}
		}		
	}
}
