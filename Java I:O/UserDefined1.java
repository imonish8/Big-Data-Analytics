class EmployeeNotFoundException extends Exception {
		private static final long serialVersionUID = -2930445672727272L;
		

		private int id;

		EmployeeNotFoundException (int i, String message){
			super(message);
			this.id = id;
			
		}
		EmployeeNotFoundException(int i, String message, String cause){
			super(message, new Throwable(cause));
			this.id = id;
		}
		@Override
		public String toString(){
			return String.format("EmployeeNotFoundException[%d]", this.id);
		}		
		
}
		public class UserDefined{
			public static void main(String[] args){
				int id = 1001;
				try{
					if(id != 1000){
						throw new EmployeeNotFoundException(id, "Employee may not be Available", "Resigned");
					}
				}catch(EmployeeNotFoundException exp){
						System.out.println(exp.getMessage());
						exp.printStackTrace();
			}
		}

}

