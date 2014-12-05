import java.io.*;
import java.net.*;


public class Web
{
	public static void main(String[] args)
	{
	    URL url;
	    InputStream is = null;
	    BufferedReader br;
	    String line;

	    try
	    {
	        url = new URL("http://iptest.malwarebytes.org/");
	        //is = url.openStream();  // throws an IOException
	        url.openConnection().connect();
	        is = url.openStream();
	        br = new BufferedReader(new InputStreamReader(is));

	        while ((line = br.readLine()) != null)
	        {
	            System.out.println(line);
	        }
	    }
	    catch(Exception ex)
	    {
	    	
	    	ex.printStackTrace();
	    }
	}
}
