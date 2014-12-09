import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.text.DecimalFormat;

import javax.imageio.ImageIO;


public class Stensil
{
	private BufferedImage bi;
	private final int SIZE = 50;
	
	public Stensil(String file) throws IOException
	{
		File f = new File(file);
		if(!f.exists())
		{
			bi = new BufferedImage(SIZE, SIZE, BufferedImage.TYPE_INT_ARGB);
			ImageIO.write(bi, "png", f);
		}
		bi = ImageIO.read(new File(file));
	}
	
	public int[][] encode(String s)
	{
		int[][] colors = new int[s.length()][4];
		
		for(int i = 0; i < s.length(); i++)
		{
			String brep = intToBinary((int)s.charAt(i));
			int r = Integer.parseInt(brep.substring(0,2));
			int g = Integer.parseInt(brep.substring(2,4));
			int b = Integer.parseInt(brep.substring(4,6));
			int a = Integer.parseInt(brep.substring(6,8));
			
			colors[i][0] = r;
			colors[i][1] = g;
			colors[i][2] = b;
			colors[i][3] = a;
		}
		return colors;
	}
	
	public String intToBinary(int num)
	{
		String newString = Integer.toBinaryString(num);
		return newString;
	}
	
	public int binaryToInt(String bin)
	{
		return Integer.parseInt(bin, 2);
	}
	
	public static void main(String args[]) throws IOException
	{

		Stensil ste = new Stensil("output.png");

		int i = 49;
		System.out.printf("Expected: %S\n", Integer.toBinaryString(i));
		System.out.printf("Actual:   %S\n", ste.intToBinary(i));
	}
}