public class Priorities implements Runnable {

	public void run(){
		System.out.println(Thread.currentThread());
	}
	public static void main(String[] args){
		Priorities p1 = new Priorities();
		Thread t1 = new Thread(p1, "First Thread");
		Thread t2 = new Thread(p1, "Second Thread");
		Thread t3 = new Thread(p1, "Third Thread");
	
		t1.setPriority(4);
		t2.setPriority(3);
		t3.setPriority(8);
	
		t1.start();
		t2.start();
		t3.start();
	}
}
