import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.AbstractButton;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;

public class EnhancedClipboard {
	JFrame frame;
	JPanel panel;
	JButton button;
	JTextField text;
	JCheckBox check;
	
	public EnhancedClipboard(){
		frame = new JFrame();
		panel = new JPanel();
		button = new JButton("Copy");
		text = new JTextField(8);
		check = new JCheckBox("Editable", true);
		
		ActionListener checklist = new ActionListener(){
			public void actionPerformed(ActionEvent e){
				boolean selected = ((AbstractButton) e.getSource()).getModel().isSelected();
				if (selected){
					text.setEditable(true);
				} else {
					text.setEditable(false);
				}
			}
		};
		check.addActionListener(checklist);
		
		
		ActionListener buttonlist = new ActionListener(){
			public void actionPerformed(ActionEvent e){
				StringSelection selection  = new StringSelection(text.getText());
			    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
			    clipboard.setContents(selection , selection);
			}
		};
		button.addActionListener(buttonlist);
		
		panel.add(button);
		panel.add(text);
		panel.add(check);
		frame.add(panel);
		frame.pack();
		frame.setAlwaysOnTop(true);
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public static void main(String[] args){
		new EnhancedClipboard();
	}
}
