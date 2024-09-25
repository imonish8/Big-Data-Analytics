public class Synchronized implements Runnable {

	int tickets = 3;
	static int i = 1, j = 2, k = 3;
	
	synchronized void bookticket(String name, int wantedTickets){
		
		if(wantedTickets <= tickets){
			System.out.println(wantedTickets +" booked to "+name);
		}else{
			System.out.println("No Tickets to Book");
		}
	}
	
	public void run(){	
		
		String name = Thread.currentThread().getName();
			
			if(name.equals("t1")){
				bookticket(name, i);
			}else if (name.equals("t2")){
				bookticket(name, j);
			}else{
				bookticket(name, k);
			}
	}

	public static void main(String[] args){
		
		Synchronized s = new Synchronized();
		
		Thread t1 = new Thread(s);
		Thread t2 = new Thread(s);
		Thread t3 = new Thread(s);

		t1.setName("t1");
		t2.setName("t2");
		t3.setName("t3");

		t1.start();
		t2.start();
		t3.start();
	}
}
