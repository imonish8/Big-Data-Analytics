public class logical{
		public static void main(String[] args){
			boolean placement = true;
			boolean future = true;
			
			if(placement&&future){
			System.out.println("\n (Placement && Future) :"+(placement&&future));
			System.out.println("\n (Placement || Future):"+(placement || future));
			System.out.println("\n !(Placement && Future):"+!(placement && future));
			}	
	}
}
