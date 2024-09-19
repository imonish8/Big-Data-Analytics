public class gc_request{

		public static void main(String[] args){

		gc_request t = new gc_request();
		t=null;
		System.gc();	
	}
		public void finalize(){

		System.out.println("Garbage collection");
		}
	
}
