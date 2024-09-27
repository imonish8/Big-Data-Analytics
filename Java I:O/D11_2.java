abstract class Customer {

    abstract void getInputs();
    abstract void display();
    abstract void order();
    
}

class RetailCustomer extends Customer {

  private String name;
  private String address;
  private int orderAmount;
  
  void getInputs() {
  
    this.name = "Monish Nule";
    this.address = "Pune";
    this.orderAmount = 5;
  
  
  }
  
  void display() {
  
      System.out.println("Retail CUstomer Details");
      System.out.println("Name "+name);
      System.out.println("Address :" + address);
      System.out.println("Order Amount "+ orderAmount+ " items");
}

  void order() {
  
    System.out.println("Retail Order of "+ orderAmount + "Items Placed");
    }
}

class WholesaleCustomer extends Customer {

      private String companyName;
      private String companyAddress;
      private int bulkOrderAmount;
      
      void getInputs(){
        this.companyName = "Wholesale INC.";
        this.companyAddress = "345 Wholesale Avenue";
        this.bulkOrderAmount = 1000;
      }
      
      void display() {
      
        System.out.println("WHolesale CUstomer Details");
        System.out.println("Company NAme "+ companyName);
        System.out.println("Company Address "+ companyAddress);
        System.out.println("Bulk Order amount "+ bulkOrderAmount+ " items");
      }
      
      void order() {
      
        System.out.println("Wholesale bulk order of "+bulkOrderAmount+ " items");
        }
  }
  
  public class D11_2 {
      public static void main(String args[]) {
      
        RetailCustomer rc = new RetailCustomer();
        rc.getInputs();
        rc.display();
        rc.order();
        
        System.out.println();
        
        WholesaleCustomer wc = new WholesaleCustomer();
        wc.getInputs();
        wc.display();
        wc.order();
        
      }
  }
