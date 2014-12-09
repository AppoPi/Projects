import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.io.File;


public class Test
{
	String THIRTY_TWO_BIT = "C:\\Program Files";
	String SIXTY_FOUR_BIT = "C:\\Program Files (x86)";
	Process p;
	
	public boolean is64()
	{
		File f = new File(THIRTY_TWO_BIT);
		
		return f.isDirectory();
	}
	
	public String getMBAMDirectory()
	{
		String s = "";
		if(is64())
		{
			s += SIXTY_FOUR_BIT; 
		}
		else
		{
			s += THIRTY_TWO_BIT;
		}
		return s + "\\Malwarebytes Anti-Malware\\mbam.exe";
		
	}
	
	public boolean MBAMisInstalled()
	{
		File f = new File(getMBAMDirectory());
		return f.exists();
	}
	
	public boolean installMBAM()
	{
		String path = "\"" + System.getProperty("user.home") + "\\Desktop\\2013-12-12_10-04-56 (175)\\mbam-setup-consumer-2.00.0.0025.exe\"";
		try
		{
			p = Runtime.getRuntime().exec(path);
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
		return true;
	}
	
	public boolean openMBAM()
	{
		if(MBAMisInstalled())
		{
			try
			{
				p = Runtime.getRuntime().exec(getMBAMDirectory());
			}
			catch(Exception e)
			{
				return false;
			}
			return true;
		}
		return false;
	}
	
	public static void main(String[] args) throws Exception
	{
		Test t = new Test();
		t.installMBAM();
		
	}
	
	//--On Premium
	//Dashboard
	//Fix Now
	//License Details
}
