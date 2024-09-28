import java.util.*;
public class ThreadwRunnable implements Runnable {
		public void run() {
			System.out.println("My Thread is Running");
		}
	public static void main(String[] args){
		
		Runnable obj_runnable = new ThreadwRunnable();
		Thread obj_thread = new Thread(obj_runnable);

		obj_thread.start();
	}
}
