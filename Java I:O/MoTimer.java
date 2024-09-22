import javax.swing.*;
import java.awt.event.*;
public class MoTimer {

		//public static void main(String[] args){
			private static int seconds = 0;
			private static Timer timer;
	
		public static void main(String[] args){	
			
			// JFrame ui Settings.
			JFrame frame = new JFrame("Simple Timer");
			frame.setSize(300, 150);
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setLayout(null);
			
			//Label to display timer
			JLabel timerLabel = new JLabel("Time: 0 seconds", SwingConstants.CENTER);
			frame.add(timerLabel);
			

			JButton startbutton = new JButton("Start Timer");
			startbutton.setBounds(50, 70, 100, 30);
			frame.add(startbutton);

			JButton stopButton = new JButton("Time: "+seconds+" seconds");
			stopButton.setBounds(160, 70, 100, 30);
			frame.add(stopButton);
	
			timer = new Timer (1000, new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					seconds++;
					timerLabel.setText("Time :"+seconds+" seconds");
				}
			});
			
			startbutton.addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					timer.start();
				}
			});
		
			stopButton.addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					timer.stop();
				}
			});
			
			frame.setVisible(true);
		}
}
