import java.util.*;
class Campusdata{
	int blgno;
	float area;
	String loca;
	int noOfCafe;
	Campusdata(int blgno, float area, String loca, int noOfCafe){
		this.blgno = blgno;
		this.area = area;
		this.loca = loca;
		this.noOfCafe = noOfCafe;

	}
	
	public String toString(){
		return("\nBuilding No:"+blgno+"\nArea of Campus in acres :"+area+"\nLocation of the Campus :"+loca+"\nNo of Cafeteria campus has :"+noOfCafe);
	}
}

public class Campus {
		public static void main(String[] args) {

		Campusdata d1 = new Campusdata(11, 55.33f, "North-West Pune", 12);
		ArrayList<Campusdata> campuslist = new ArrayList<>();
		campuslist.add(d1);
		System.out.println(campuslist);
		Campusdata cobj;
		Iterator itr = campuslist.iterator();
		while(itr.hasNext()){
			System.out.println(itr.next());
		}
	}
}
