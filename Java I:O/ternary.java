public class ternary{
		public static void main(String[] args){
			int num1, num2 =0;
			num1 = 25;
			num2 = (num1 == 10) ? 100:200;
			System.out.println("Num 2 when num1==10 return false:"+num2);
			num2 = (num1 == 25) ? 100:200;
			System.out.println("Num 2 when num1==25 returns true:"+num2);		
		}
}
