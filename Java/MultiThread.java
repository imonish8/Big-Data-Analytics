class MultiThread extends Thread {

		public void run(){
			System.out.println("My Thread is running state");
			System.out.println(getName());
		}
		public void myMethod(){

			System.out.println(getName());
		}
	public static void main (String[] args){
		
		MultiThread obj = new MultiThread();
		obj.start();
		obj.myMethod();
		System.out.println("essage is here: "+obj.getName());		
		
	}
}
