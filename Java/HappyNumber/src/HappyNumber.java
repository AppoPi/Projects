import java.util.ArrayList;

public class HappyNumber
{
	static int[] already;
	
	public HappyNumber()
	{
		already = new int[1000];
	}
	public static boolean isHappy(int n) throws InterruptedException
	{
		int sum = 0;
		ArrayList<Integer> list = new ArrayList<Integer>();
		
		do
		{
			
			String s = n + "";

			for(int i=0; i<s.length(); i++)
			{
				sum += (n%10) * (n%10);
				n/=10;
				if(n==0)
					break;
			}

			n = sum;
			sum = 0;

			if(list.contains(n))
				break;
			else
				list.add(n);
		}
		while(n!=1);
		
		if(n==1)
		{
			return true;
		}
		else return false;
	}
	
	public static void main(String[] args) throws InterruptedException
	{
		for(int i=0, x=0; i<1001; i++)
		{
			if(HappyNumber.isHappy(i))
			{
				System.out.print(i + ", "); if(x%10==0 && x!=0)System.out.println();
				x++;
			}
		}
	}
}