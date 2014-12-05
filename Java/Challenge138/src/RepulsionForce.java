import java.text.DecimalFormat;
import java.util.Scanner;
import java.util.StringTokenizer;


public class RepulsionForce
{
	public static void main(String[] args)
	{
		Scanner s = new Scanner(System.in);
		System.out.print("Enter particle 1's mass, x, and y: ");
		String part1 = s.nextLine();
		System.out.print("Enter particle 2's mass, x, and y: ");
		String part2 = s.nextLine();
		StringTokenizer st = new StringTokenizer(part1, " ");
		
		double particle1_mass = Double.parseDouble(st.nextToken());
		double particle1_x = Double.parseDouble(st.nextToken());
		double particle1_y = Double.parseDouble(st.nextToken());
		
		st = new StringTokenizer(part2, " ");
		double particle2_mass = Double.parseDouble(st.nextToken());
		double particle2_x = Double.parseDouble(st.nextToken());
		double particle2_y = Double.parseDouble(st.nextToken());
		
		double deltaX = particle1_x - particle2_x;
		double deltaY = particle1_y - particle2_y;
		
		double distance_squared = deltaX * deltaX + deltaY * deltaY;
		
		double force = particle1_mass * particle2_mass / distance_squared;
		
		
		DecimalFormat df = new DecimalFormat("#.####");
		System.out.println(df.format(force));
		s.close();
	}
}
