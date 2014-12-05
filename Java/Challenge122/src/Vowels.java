import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class Vowels
{
	BufferedReader br;
	FileReader fr;
	String filename;
	
	public Vowels() throws FileNotFoundException
	{
		filename = "enable1.txt";
		open();
	}
	
	public void open() throws FileNotFoundException
	{
		fr = new FileReader(filename);
		br = new BufferedReader(fr);
	}
	
	public void close() throws IOException
	{
		br.close();
		fr.close();
	}
	
	public String[] fillArray() throws IOException
	{
		int n = 172820;
		String s, words[] = new String[n];
		for(int i=0; (s = br.readLine()) != null; i++)
		{
			words[i] = s;
		}
		return words;
	}
	
	public boolean hasAllVowels(String s)
	{
		return s.replaceAll("[^aeiouy]", "").equals("aeiouy");
	}
	
	public static void main(String[] args) throws IOException
	{
		Vowels v = new Vowels();
		v.open();
		String[] words = v.fillArray();
		for(int i=0; i<words.length; i++)
		{
			if(v.hasAllVowels(words[i]))
			{
				System.out.println(words[i]);
			}
		}
		v.close();
	}	
}
