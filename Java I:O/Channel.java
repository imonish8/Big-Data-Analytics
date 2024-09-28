import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

public class Channel{
	public static void main(String[] args) {

		RandomAccessFile file = new RandomAccessFile("MyFileRead", "r");
		FileChannel fc = file.getChannel();
		ByteBuffer bf = ByteBuffer.allocate(512);
	        bf.flip();
		while(fileChannel.read(bf) > 0){
			
			System.out.println((char)bf.get());
		}
	file.close();
	}
	
}

