import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;


public class Pinger
{
	static String filename = "C:\\Users\\alee\\Downloads\\Websites\\websites.csv";
	static String outfile = "C:\\Users\\alee\\Downloads\\Websites\\output.txt";

	//public static void main(String[] args) throws IOException, InterruptedException
	public Pinger() throws Exception
	{
		File file = new File(outfile);
		if(file.exists())
		{
			file.delete();
		}
		
		BufferedReader bf = new BufferedReader(new FileReader(filename));
		
		String site = "";
		
		BufferedWriter bw = null;
		//while((site = bf.readLine())!=null)
		for(int i = 0; i < 10; i++)
		{			
			try
			{
				bw = new BufferedWriter(new FileWriter(new File(outfile), true));
				/*
				URL url = new URL("http://" + site);
				HttpURLConnection spoof = (HttpURLConnection) url.openConnection();
				spoof.addRequestProperty("User-Agent", "Mozilla/4.76");
				*/
				
				Runtime.getRuntime().exec("start chrome " +site);
				Thread.sleep(5000);
				Runtime.getRuntime().exec("taskkill /IM chrome.exe");
				
				/*
				BufferedReader in = new BufferedReader(new InputStreamReader(spoof.getInputStream()));	

				@SuppressWarnings("unused")
				String s;
				while ((s = in.readLine()) != null){}
				*/
			}
			/*
			catch(java.net.ConnectException ex)
			{
				bw.write(site + "\n");
				bw.close();
			}
			catch(java.net.UnknownHostException ex)
			{
				//bw.write(site);
				//bw.write("\t DOWN\n");
			}
			catch(java.io.IOException ex)
			{
				//bw.write(site);
				//bw.write("\t SERVER ERROR\n");
			}
			*/
			catch(Exception ex)
			{
				ex.printStackTrace();
			}
		}
		bf.close();
	}
}
