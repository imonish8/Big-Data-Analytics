public class cmdLine{
		public static void main(String[] args){
			int cmdLen = args.length;
			System.out.println("Command Line Arguements that you have passed");
			
			for(int i=0; i<cmdLen;i++){
				System.out.println(args[i]);
			}
			if(Integer.parseInt(args[0])>=18){
				System.out.println(args[0]+" is Eligible to vote in this election");

			}
			for(int i=0; i<cmdLen; i++){
				System.out.println(i+1+"th value "+args[i]);

			}
		}
}
