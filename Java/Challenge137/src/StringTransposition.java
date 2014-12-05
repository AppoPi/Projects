import java.util.Scanner;


public class StringTransposition
{
	int length = 0;
	
	public int maxLength(String[] list)
	{
		int max = 0;
		for(int i=0; i<list.length; i++)
		{
			if(list[i].length()>max)
			{
				max = list[i].length();
			}
		}
		return max;
	}
	
	public void normalize(String[] list)
	{
		length = maxLength(list);
		
		for(int i=0; i<list.length; i++)
		{
			while(list[i].length()<length)
			{
				list[i]+=" ";
			}
		}
	}
	
	public String transpose(String[] words)
	{
		normalize(words);
		String bob = "";
		for(int j=0; j<length; j++)
		{
			for(int i=0; i<words.length; i++)
			{
				bob += words[i].charAt(j) + "";
			}
			bob += "\n";
		}
		
		return bob;
	}
	
	public static void main(String[] args)
	{
		StringTransposition st = new StringTransposition();
		Scanner s = new Scanner(System.in);
		System.out.print("Enter number of words: ");
		int size = s.nextInt();
		String[] list = new String[size];
		for(int i=0; i<size; i++)
		{
			System.out.print("Enter word #"+ (i+1) +": ");
			list[i] = s.next();
		}
		System.out.println(st.transpose(list));
		s.close();
	}
}
