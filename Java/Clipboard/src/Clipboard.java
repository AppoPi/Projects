import java.awt.GridLayout;
import java.awt.Toolkit;
import java.awt.datatransfer.StringSelection;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;


public class Clipboard
{
	
	String id1= "4TQ87-J57YF";
	String key1 = "UTDW-3E46-L8A3-3J92";

	String id2 = "id1@email.com";
	String key2 = "MBCNM-MMMAA-2JXY5-EV7SM-PHC6D";
	
	JFrame f = new JFrame();
	JPanel p = new JPanel();
	
	JLabel l1 = new JLabel("MBAM 2.0 License ID");
	JLabel l2 = new JLabel("MBAM 1.0 License Key");
	JLabel l3 = new JLabel("MBAM 2.0 License ID");
	JLabel l4 = new JLabel("MBAM 2.0 License Key");
	
	JButton t1 = new JButton(id1);
	JButton t2 = new JButton(key1);
	JButton t3 = new JButton(id2);
	JButton t4 = new JButton(key2);
	
	public Clipboard()
	{
		p.add(l1);
		p.add(t1);
		p.add(l2);
		p.add(t2);
		p.add(l3);
		p.add(t3);
		p.add(l4);
		p.add(t4);
		
		p.setLayout(new GridLayout(0,2));
		
		f.add(p);
		f.pack();
		
		t1.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent a)
			{
				Toolkit toolkit = Toolkit.getDefaultToolkit();
				java.awt.datatransfer.Clipboard clipboard = toolkit.getSystemClipboard();
				StringSelection strSel = new StringSelection(t1.getText());
				clipboard.setContents(strSel, null);
			}
		});
		
		t2.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent a)
			{
				Toolkit toolkit = Toolkit.getDefaultToolkit();
				java.awt.datatransfer.Clipboard clipboard = toolkit.getSystemClipboard();
				StringSelection strSel = new StringSelection(t2.getText());
				clipboard.setContents(strSel, null);
			}
		});

		t3.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent a)
			{
				Toolkit toolkit = Toolkit.getDefaultToolkit();
				java.awt.datatransfer.Clipboard clipboard = toolkit.getSystemClipboard();
				StringSelection strSel = new StringSelection(t3.getText());
				clipboard.setContents(strSel, null);
			}
		});

		t4.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent a)
			{
				Toolkit toolkit = Toolkit.getDefaultToolkit();
				java.awt.datatransfer.Clipboard clipboard = toolkit.getSystemClipboard();
				StringSelection strSel = new StringSelection(t4.getText());
				clipboard.setContents(strSel, null);
			}
		});
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setVisible(true);
	}
	
	public static void main(String[] args)
	{
		new Clipboard();
	}
}
