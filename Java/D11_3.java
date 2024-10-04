abstract class Course {
	int duration;
	boolean eli;
	int isPassedTen;

	abstract void Courses(int duration, int isPassedTen);
	
	

	abstract void Display();
}
class Arts extends Course{
 	int duration;
        boolean eli;
        int isPassedTen;	

	void Courses(int duration, int isPassedTen){
		this.duration = duration;
		this.isPassedTen = isPassedTen;
	}
	void Display(){
		if(isPassedTen > 60){
			eli = true;
			System.out.println("Passed tenth with "+isPassedTen+"%. Eligibility is "+eli);
		}else{
			System.out.println("Sorry, student is not Eligible for Arts.");
		}
		System.out.println("Duration of the Arts course is "+duration);
		System.out.println("Your Percentage obtained in Metrics :"+isPassedTen);
	}
		
}

class Eng extends Course{
	int duration;
        boolean eli;
        int isPassedTen;

	void Courses(int duration, int isPassedTen){
		this.duration = duration;
		this.isPassedTen = isPassedTen;
	}
	void Display(){
                if(isPassedTen > 60){ 
                        eli = true;
                        System.out.println("Passed tenth with "+isPassedTen+"%. So can take admission in Engineering Courses.");
	
                }else{ 
                        System.out.println("Sorry, student is not Eligible for ANY Engineering Courses");
	
                } 
                System.out.println("Duration of the Engineering course is "+duration);
                System.out.println("Your Percentage obtained in Metrics are "+isPassedTen);

        } 



}

public class D11_3 {
	public static void main(String args[]) {
		Course Student1 = new Arts();
		Student1.Courses(3, 50);
		Student1.Display();
		
	}
}
