class Student implements Runnable{
	private String task;
	
	Student(String task){
		this.task = task;
	}

	public void run(){
		System.out.println(task+"  Running");

	try{

		int worktime = (int) (Math.random() * 5000);
		Thread.sleep(worktime);
		System.out.println(task+"   completed in  "+worktime+"  milliseconds");
	}catch (Exception e){
		System.out.println("Exception is thrown, message is :"+e.getMessage());
	}


	}
}


public class D20 {
	public static void main(String[] args){
	
	Thread t1 = new Thread(new Student("Student going Home"));
	Thread t2 = new Thread(new Student("Student going Tution"));
	Thread t3 = new Thread(new Student("Student going Classes"));
	Thread t4 = new Thread(new Student("Stduent going Tennis"));
	Thread t5 = new Thread(new Student("Student going swimming"));
	Thread t6 = new Thread(new Student("Student going Vacations"));
	Thread t7 = new Thread(new Student("Student going Holidays"));
	Thread t8 = new Thread(new Student("Student going Shop"));
	Thread t9 = new Thread(new Student("Student going Cafeteria"));
	Thread t10 = new Thread(new Student("Student goint ClubHouse"));

	t1.start();
	t2.start();
	t3.start();
	t4.start();
	t5.start();
	t6.start();
	t7.start();
	t8.start();
	t9.start();
	t10.start();



	}	
}
