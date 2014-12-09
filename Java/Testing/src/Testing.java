import java.io.*;

public class Testing
{
	public String path;
	public String file;
	public String symbols;
	
	public Testing()
	{
		path = "C:\\Users\\alee\\Desktop\\Test\\";
		file = "test-trojan.exe";
	}
	
	public void copy(String source, String dest) throws IOException
	{
		File s = new File(source);
		File d = new File(dest);
		copyFileUsingFileStreams(s,d);
	}
	
	private void copyFileUsingFileStreams(File source, File dest) throws IOException
	{
	    InputStream input = null;
	    OutputStream output = null;

	    try
	    {
	        input = new FileInputStream(source);
	        output = new FileOutputStream(dest);
	        byte[] buf = new byte[1024];
	        int bytesRead;
	        
	        while ((bytesRead = input.read(buf)) > 0)
	        {
	            output.write(buf, 0, bytesRead);
	        }

	    }
	    finally
	    {
	        input.close();
	        output.close();
	    }
	}

	public static void main(String[] args) throws IOException
	{
		Testing t = new Testing();		

		
		//Characters 1-31 128 to 160 (inclusive) are not printable
		for(int i = 32; i <= 15000; i++)
		{
			String s = (char) i + "";
			
			//Filenames cannot contain these symbols: \\ / : * ? \" < > |
			if(!"\\ / . : * ? \" < > |".contains(s))
			{
				//Create filename
				String num = String.format("%05d", i);
				String sb = t.path + "extra\\" + num + " " + s + ".exe";
				
				//Create file with special character name
				System.out.println(sb.toString());
				t.copy(t.path + t.file, sb.toString());

				//Make directory with special character and put corresponding file into it
				File newdir = new File(t.path + "extra\\" + num + " " + s);
				
				newdir.mkdir();
				t.copy(t.path + t.file, newdir.getAbsolutePath() + "\\" + num + " " + s + ".exe");
			}
		}
	}
}


