import java.text.DecimalFormat;
import java.util.Random;

public class Monty
{
	Random r;
	DecimalFormat df;
	String pattern = "##.00%";
	
	public Monty()
	{
		r = new Random();
		df = new DecimalFormat(pattern);
	}
	
	public int choose(int doors)
	{
		return r.nextInt(doors);
	}
	
	public int[] play(int doors, int rounds)
	{
		int withoutswitch = 0;
		int withswitch = 0;
	
		for(int i=0; i<rounds; i++)
		{
			int prize = choose(doors);
			int choice = choose(doors);
			int temp = withoutswitch;
			
			if(choice == prize)//1st guess
			{
				withoutswitch++;
				continue;
			}

			if(temp == withoutswitch)//Was not right 1st guess
			{
				int newchoice = 0;
				int open = 0;
				while(open==prize || open==choice)//Opened goats door
				{
					open++;
				}
				while(newchoice==choice || newchoice==open)//Switch to not 1st guess/opened goat door
				{
					newchoice++;
				}
				if(prize==newchoice) withswitch++;//Second guess
			}
		}
		return new int[]{withoutswitch, withswitch};
	}
	
	public String print(int[] wins, int timesplayed)
	{
		String tactic1 = df.format((double)wins[0]/(double)timesplayed);
		String tactic2 = df.format((double)wins[1]/(double)timesplayed);
		
		return "Tactic 1: " + tactic1 + " winning chance\n" + "Tactic 2: " + tactic2 + " winning chance";
	
	}
	
	public static void main(String[] args)
	{
		Monty m = new Monty();
		
		int timesplayed = 1000000000;
		
		int wins[] = m.play(3, timesplayed);
		
		System.out.println(m.print(wins, timesplayed));
	}
}
