class Count extends Thread {
	


	Count(){
		super("My extending Thread");
		System.out.println("My Thread");
		start();
	}
	public void run(){
		try{
			for(int i=0;i<10;i++){
				System.out.println("Printing the count "+i);
				Thread.sleep(1000);
			}
		}catch (InterruptedException e){
			System.out.println("my Thread is Interrupted");
		}
		System.out.println("My THread run is over");
	}
}

class MultiThreading {
	public static void main(String[] args){
	
		Count cnt = new Count();
		try{
			while(cnt.isAlive()){
		System.out.println("Main tHREAD WIL BE ALIVE TILL THE CHILD THREAD IS LIVE");

			Thread.sleep(1300);
			}
		}catch (InterruptedException e){
			System.out.println("Main Threas interrupted");
		}
		System.out.println("Main Thread's run is over");
		}
	}

