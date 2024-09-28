class Student implements Serialization {
	int id;
	String name;
	long phno;
	String 
import java.io.*;


 class Studentinfo implements Serializable
 {
 String name;
 int rid;
 static String contact;
 Studentinfo(String n, int r, String c)
 {
 this.name = n;
 this.rid = r;
 this.contact = c;
 }
 }

public  class Series 
 {
 public static void main(String[] args)
 {
 Studentinfo si=null ;
 try
 {
 FileInputStream fis = new
FileInputStream("/filepath/stud.txt");
 ObjectInputStream ois = new ObjectInputStream(fis);
 si = (Studentinfo)ois.readObject();
 }
 catch (Exception e)
 {
 e.printStackTrace(); }
 System.out.println(si.name);
 System.out. println(si.rid);
 System.out.println(Studentinfo.contact);
 }
 }
