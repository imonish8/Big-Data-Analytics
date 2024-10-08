public class Room{
	int roomNo;
	String roomType;
	double roomArea;
	boolean hasAC;

	public void setData(int roomNo, String roomType, double roomArea, boolean hasAC){
	
		this.roomNo = roomNo;
		this.roomType = roomType;
		this.roomArea =roomArea;
		this.hasAC = hasAC;
	}


	public void displayData(){

		System.out.println("Room Number : "+roomNo);
		System.out.println("Room Type : "+roomType);
		System.out.println("Room Area : "+roomArea);
		System.out.println("AC Available :"+hasAC);
	}


	public static void main(String[] args){

		Room room = new Room();
		room.setData(10001, "Delux", 250.5, true);
		room.displayData();
	}
}
