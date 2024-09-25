class ThreadEx implements Runnable{
	public static void main(String[] args){
		
		Thread t1 = new Thread("Thread 1 running");
		Thread t2 = new Thread("Thread 2 Running");
	
		t1.start();
		
		/*try{
			t1.sleep(5000);
			t1.start();
		}catch(InterruptedException e){

			System.out.println("Sleep doesnt make sense");
		}*/	
		t2.start();
		
		System.out.println("T 1 Running "+t1.getName());	
		System.out.println("T2 Runnning "+t2.getName());
	}
	
	public void run(){
		Thread temp = Thread.currentThread();
		//System.out.println(temp.getName().currentThread());
		//temp.sleep(5000);
		System.out.println(temp.getName());	
	}
}
