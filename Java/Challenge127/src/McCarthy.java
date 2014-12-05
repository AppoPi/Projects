
public class McCarthy
{
	public void mc(int n)
	{
		System.out.println("M(" + n + ")");
		mc91(n);
	}
	public int mc91(int n)
	{		
		if (n>100)
		{
			System.out.println("M(" + n + "-10) since " + n + " is greater than 100");
			return n-10;
		}
		else
		{
			System.out.println("M(M(" + n + "+11) since " + n + " is equal to or less than 100");
			return mc91(mc91(n+11));
		}
	}
	
	public static void main(String[] args)
	{
		McCarthy mc = new McCarthy();
		mc.mc(99);
	}
}
