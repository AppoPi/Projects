
public class Sum
{
	public int sumThemDigits(int num)
	{
		int sum=0, newnum=num;
		do
		{
			while(newnum>0)
			{
				for(sum=0; newnum>0; newnum/=10)
				{
					sum+=newnum%10;
				}
			}
			newnum=sum;
		}
		while(sum>9);
		return sum;
	}
	
	public static void main(String[] args)
	{
		Sum s = new Sum();
		System.out.println(s.sumThemDigits(31337));
		System.out.println(s.sumThemDigits(1073741824));
	}
}
