public class D21_2 {
	public static void main(String[] args) {

	Thread t1 = new Thread(new Runnable() {
	
	public void run(){
		System.out.println("Thread 1 is Running ");
		for(int i = 0; i<= 5; i++){

			System.out.println("Thread 1 Count :"+i);
		}

		int worktime = (int) (Math.random() * 5000);
		try{
		Thread.sleep(worktime);
		}catch (InterruptedException e){
			System.out.println(e.getMessage());
		}
		System.out.println("Thread 1 were Busy for  "+worktime);

	}	
	

	});


	Thread t2 = new Thread(new Runnable() {
	
		public void run() {
	
		System.out.println("Thread 2 is Running");
		for(int i = 0; i<= 7; i++){
			System.out.println("Thread 2 Count : "+i);
		}
		int worktime = (int) (Math.random() * 5000);
		try{
		Thread.sleep(worktime);
		}catch (InterruptedException e){
			System.out.println(e.getMessage());
		}
		System.out.println("Thread 2 is busy for "+worktime+" Milliseconds");
	
		}
	});

	Thread t3 = new Thread(new Runnable() {

		public void run(){
		System.out.println("Thread 3 is running");
		for(int i =0; i<= 10; i++){
			System.out.println("Thread 3 Count : "+i);
		}
		int worktime  = (int) (Math.random() * 5000);
		try{
		Thread.sleep(worktime);
		}catch (InterruptedException e){
			System.out.println(e.getMessage());
		}
		System.out.println("Thread 3 is busy for "+worktime+" milliseconds");
		
	}
	});

	t1.start();
	t2.start();
	t3.start();
}
}
