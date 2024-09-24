class ThreadEx implements Thread{
	public static void main(String[] args){
		Thread(String name ){
		super(name);
		}
		Thread t1 = new Thread("Thread 1 running");
		Thread t2 = new Thread("Thread 2 Running");
	
		t1.start();
		t2.start();
		
		System.out.println("T 1 Running "+t1.getName());	
		System.out.println("T2 Runnning "+t2.getName());
	}
	
	public void run(){
/*
		Thread temp = Thread.currentThread();
		System.out.println(temp.getName().currentThread());	
*/
	}
}
