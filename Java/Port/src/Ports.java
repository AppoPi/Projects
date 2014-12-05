import java.io.IOException;
import java.net.ServerSocket;


public class Ports
{
	/**
	 * Checks to see if a specific port is available.
	 *
	 * @param port the port to check for availability
	 */
	public static void main(String[] args)
	{		
		for(int port=0; port<60000;port++)
		{
		    ServerSocket socket = null;
		    try
		    {
		        socket = new ServerSocket(port);
		    }
		    catch (IOException e)
		    {
		    	
		    }
		    finally
		    {
		        if (socket != null)
		        {
		            try
		        	{
		                socket.close();
		            }
		        	catch (IOException e)
		        	{
		        		/* e.printStackTrace(); */
		        	}
		        }
		        else
		        {
		        	System.out.println(port);
		        }
		    }
		}
	}
}
