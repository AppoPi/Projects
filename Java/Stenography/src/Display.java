
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;

import javax.swing.JPanel;
import javax.swing.JFrame;


public class Display extends JPanel
{
	private static final long serialVersionUID = 8153251123L;
	//User Interface Frame
	private static JFrame myFrame;
	private static Graphics2D g2;
	//Number of rows and tile width and height
	private final int rows;
	private final int width;
	private final int height;
	//2D Array of Colors recording RGB values of each square
	private Color[] colored;
	private int perRow;
	
	public Display(String s)
	{
		setDoubleBuffered(true);
		
		//Initialize variables
		myFrame = new JFrame();
		rows = s.length();
		int size = 20;
		width = height = size;
		colored = new Color[s.length()];		
		
		//Generate color
		Encode e = new Encode();
		int[][] generated = e.encode(s);

		
		//System.out.println("---DISPLAY---");
		for(int i = 0; i < s.length(); i++)
		{
			int[] color1 = generated[i];
			Color c = new Color(color1[0],color1[1],color1[2],color1[3]);
			colored[i] = c;
			//System.out.println(c);
		}
		
		perRow = (int)Math.ceil(Math.sqrt(rows));
		if(perRow == 0)
		{
			System.err.println("Error: cannot encode strings with length less than 1.");
			System.exit(1);
		}
	}

	public void open()
	{		
		System.setProperty("sun.awt.noerasebackground", "true");
		myFrame.setResizable(false);
		myFrame.setTitle("Stenography");
		myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		myFrame.setVisible(true);
		myFrame.setSize(width * perRow + 50, width * (rows/perRow + 1) + 75);
		
		
	}

	public void setColor(int row, int r, int g, int b, int a)
	{
		Color newColor = new Color(r,g,b,a);
		g2.setColor(newColor);
		
		Font f = new Font("Courier", Font.PLAIN, 10);
		
		g2.setFont(f);
		
		int xpos = row % perRow * width + 20;
		int ypos = row / perRow * width + 25;

		g2.fill(new Rectangle(xpos, ypos, width, height));
		
		g2.setColor(Color.BLACK);
		g2.drawString(row + 10 + "", xpos, ypos + 10);
		
		g2.draw(new Rectangle(xpos, ypos, width, height));
		
		g2.drawRect(20, 25, perRow * width, (perRow-1) * width);
		
		colored[row] = newColor;
	}
	
	public void paintComponent(Graphics graphics)
	{
		g2 = (Graphics2D) graphics;

		g2.setColor(Color.WHITE);
		g2.fill(new Rectangle(-5000, 5000, 10000, 10000));
		
		for(int i=0; i<rows; i++)
		{
			final int OR = 0;
			int r = colored[i].getRed() ^ OR;
			int g = colored[i].getGreen() ^ OR;
			int b = colored[i].getBlue() ^ OR;
			int a = colored[i].getAlpha() ^ OR;
			
			setColor(i,r,g,b,a);
		}		
	}
	
	public static void main(String[] args)
	{
		String input = "Hey, check it out! I made a program that encodes text characters into colored squares on the screen.";
		//input = "ABCDEGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyxz1234567890!@#$%^&*()_+";
		//input = "Steganography (Listen) is the art or practice of concealing a message, image, or file within another message, image, or file. The word steganography is of Greek origin and means covered writing or concealed writing. Some implementations of steganography which lack a shared secret are forms of security through obscurity, whereas key-dependent steganographic schemes adhere to Kerckhoffs's principle.[1] It combines the Greek words steganos, meaning covered or protected, and graphei meaning writing. The first recorded use of the term was in 1499 by Johannes Trithemius in his Steganographia, a treatise on cryptography and steganography, disguised as a book on magic. Generally, the hidden messages will appear to be (or be part of) something else: images, articles, shopping lists, or some other cover text. For example, the hidden message may be in invisible ink between the visible lines of a private letter.The advantage of steganography over cryptography alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages—no matter how unbreakable—will arouse interest, and may in themselves be incriminating in countries where encryption is illegal.[2] Thus, whereas cryptography is the practice of protecting the contents of a message alone, steganography is concerned with concealing the fact that a secret message is being sent, as well as concealing the contents of the message.Steganography includes the concealment of information within computer files. In digital steganography, electronic communications may include steganographic coding inside of a transport layer, such as a document file, image file, program or protocol. Media files are ideal for steganographic transmission because of their large size. For example, a sender might start with an innocuous image file and adjust the color of every 100th pixel to correspond to a letter in the alphabet, a change so subtle that someone not specifically looking for it is unlikely to notice it.";

		Display display = new Display(input);
		//System.out.println(input);
		
		myFrame.add(display);
		
		display.open();
		
		myFrame.repaint();
	}
}