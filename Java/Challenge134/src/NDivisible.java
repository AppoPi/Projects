import java.util.Scanner;
import java.util.StringTokenizer;



public class NDivisible
{
	public int ndivide(int digits, int divisor)
	{
		int num = (int)Math.pow(10, digits)-1;
		
		return num - (num%divisor);
	}
	
	public static void main(String[] args)
	{
		NDivisible nd = new NDivisible();
		Scanner s = new Scanner(System.in);
		StringTokenizer st = new StringTokenizer(s.nextLine());
		int digits = Integer.parseInt(st.nextToken());
		int divisor = Integer.parseInt(st.nextToken());
		System.out.println(nd.ndivide(digits, divisor));
		s.close();
	}
}
