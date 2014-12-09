import java.text.DecimalFormat;
import java.util.Scanner;
import java.util.StringTokenizer;


public class EasyGrading
{
	public double average(double[] grades)
	{
		double total = 0;
		for(int i=0; i<grades.length; i++)
		{
			total+= grades[i];
		}
		return total/grades.length;
	}
	
	public String round2(double x)
	{
		DecimalFormat df = new DecimalFormat("#.00");
		return df.format(x);
	}
	
	public static void main(String[] args)
	{
		Scanner s = new Scanner(System.in);
		String line1 = s.nextLine();
		StringTokenizer st = new StringTokenizer(line1);
		int students = Integer.parseInt(st.nextToken());
		int assignments = Integer.parseInt(st.nextToken());
		
		String[] classroom = new String[students];
		double[][] grades = new double[students][assignments];
		for(int i=0; i<students; i++)
		{
			classroom[i] = s.next();
			for(int j=0; j<assignments; j++)
			{
				grades[i][j] = Integer.parseInt(s.next());
			}
		}
		
		System.out.println("=-=-=-=-=-=-=-=-=-=-=");
		EasyGrading eg = new EasyGrading();		
		
		double[] finalgrades = new double[students];
		for(int i=0; i<students; i++)
		{
			finalgrades[i] = eg.average(grades[i]);
		}
		System.out.println(eg.round2(eg.average(finalgrades)));
		for(int i=0; i<students; i++)
		{
			System.out.println(classroom[i] + " " + eg.round2(eg.average(grades[i])));
		}
		s.close();
	}
}
