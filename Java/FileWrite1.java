import java.io.*;
class FileWrite1
{
public static void main(String args[])
{
try{
File f1=new File("MyFileRead.txt");
FileWriter br=new FileWriter(f1);
BufferedReader br1=new BufferedReader(new InputStreamReader(System.in));

String str;
while(!(str=br1.readLine()).equals("EOF"))

br.write(str+"\n");


br.close();


}catch(IOException ie)
{ie.printStackTrace();}
}
}
