

public class Encode
{
	public int[][] encode(String s)
	{
		int[][] colors = new int[s.length()][4];
		for(int i = 0; i < s.length(); i++)
		{
			int[] generated = convertToColor(s.charAt(i));
			colors[i][0] = generated[0] * 20;
			colors[i][1] = generated[1] * 20;
			colors[i][2] = generated[2] * 20;
			colors[i][3] = generated[3] * 20;
		}
		/*
		//System.out.println("---ENCODE---");
		for(int i = 0; i < s.length(); i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(j==0)
				{
					System.out.print("[" + colors[i][j] + ",");
				}
				else if(j<3)
				{
					System.out.print(colors[i][j] + ",");
				}
				else
				{
					System.out.println(colors[i][j] + "]");
				}
			}
		}
		*/
		
		return colors;
	}

	
	public int[] convertToColor(char a)
	{
		String s = convertToBinary(a);
		
		int[] colors = new int[4];
		
		colors[0] = Integer.parseInt(s.substring(0, 2));
		colors[1] = Integer.parseInt(s.substring(2, 4));
		colors[2] = Integer.parseInt(s.substring(4, 6));
		colors[3] = Integer.parseInt(s.substring(6, 8));
		
		return colors;
	}
	
	private String convertToBinary(int num)
	{
		String b = "";
		for(int i = 0; i < 8 ; i++)
		{
			b = num % 2 + b;
			num /= 2;
		}
		return b;
	}
	
	@SuppressWarnings("unused")
	private char convertToAscii(String s)
	{
		int sum = 0;
		for(int i = 0; i < 8; i++)
		{
			sum += s.charAt(s.length()-1-i) * Math.pow(2,i);
		}
		return (char) sum;
	}
}
