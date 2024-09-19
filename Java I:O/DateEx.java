import java.util.Calendar;
import java.util.*;
import java.text.*;
public class dateEx{
		public static void main(String[] args){
		//Calling System with its method currentTimeMillis

		long millis = System.currentTimeMillis();	
		//instantiate Date class

		Date date = new Date();
		System.out.println(date);
		System.out.println(millis);

		//instantiate the dateformat class which has format method in it, which returns string.
		//under text

		DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd hh:mm:ss");
	
		String strDate = dateFormat.format(date);
		System.out.println(strDate);

		//instantiate Calender class, under util
	
		Calendar calendar = Calendar.getInstance();
		System.out.println("The current date is "+Calendar.getTime());
		
		//METHODS UNDER CALENDER CANNOT INHERIT.

		System.out.println(Calendar.DATE, -15);
		System.out.println(Calendar.MONTH, 4);
		System.out.println(Calendar.YEAR, 2);
	}
}
