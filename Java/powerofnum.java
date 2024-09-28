class powerofnum{
		static double res;
		static double powerof(double n, double m){
			res = Math.pow(n, m);
			return res;
		}
		public static void main(String[] args){
		double result = powerof(4, 2);
		System.out.println(result);
		}
}
