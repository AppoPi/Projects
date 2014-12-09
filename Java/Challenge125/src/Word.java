import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.StringTokenizer;


public class Word
{
	BufferedReader br;
	FileReader fr;
	String filename;
	StringBuilder sb;
	HashMap<String, Integer> words;
	HashMap<Character, Integer> letters;
	int[] lettercount;
	
	public Word() throws FileNotFoundException
	{
		filename = "lorem_ipsum.txt";
		sb = new StringBuilder();
		open();
		words = new HashMap<String, Integer>();
		letters = new HashMap<Character, Integer>();
		lettercount = new int[26];
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
	
	public boolean loadText() throws IOException
	{		
		String s;
		while((s = br.readLine()) != null)
		{
			sb.append(s.toLowerCase()+" ");
		}
		return true;
	}
	
	public String getText()
	{
		return sb.toString();
	}
	
	public void addWord(String s)
	{
		if(words.containsKey(s))
		{
			words.put(s, words.get(s)+1);
		}
		else
		{
			words.put(s, 1);
		}
	}
	
	public String getThreeWords()
	{
		StringBuilder s = new StringBuilder();
		Iterator<String> iterator = words.keySet().iterator();
		s.append("Top three words: ");
		try
		{
			for(int i=0; i<3; i++)
			{
				String key = iterator.next();
				s.append("\"" + key + "\",");
			}
		}
		catch(Exception ex)
		{
			System.err.println("Not enough unique words");
		}
		return s.toString().substring(0,s.toString().length()-1);
	}
	
	public void sort()
	{
	   List<String> mapKeys = new ArrayList<String>(words.keySet());
	   List<Integer> mapValues = new ArrayList<Integer>(words.values());
	   Collections.sort(mapValues, Collections.reverseOrder());
	   Collections.sort(mapKeys, Collections.reverseOrder());
	   LinkedHashMap<String,Integer> sortedMap = new LinkedHashMap<String,Integer>();
	   Iterator<Integer> valueIt = mapValues.iterator();
	   
	   while (valueIt.hasNext())
	   {
	       Object val = valueIt.next();
	       Iterator<String> keyIt = mapKeys.iterator();

	       while (keyIt.hasNext())
	       {
	           Object key = keyIt.next();
	           String str1 = words.get(key).toString();
	           String str2 = val.toString();

	           if (str1.equals(str2))
	           {
	        	   words.remove(key);
	               mapKeys.remove(key);
	               sortedMap.put((String)key, (Integer)val);
	               break;
	           }
	       }
	   }
	   words = sortedMap;
	}
	
	public void addLetters(String s)
	{
		s=s.toLowerCase();
		for(int i=0; i<s.length(); i++)
		{
			lettercount[s.charAt(i)-97]++;
		}
	}
	
	public String getThreeLetters()
	{
		char one = ' ';
		int high = -1;
		int NUM_OF_LETTERS = 26;
		for(int i=0; i<NUM_OF_LETTERS; i++)
		{
			if(lettercount[i]>high)
			{
				high = lettercount[i]; 
				one = (char)('a'+i);
			}
		}
		
		high =-1;
		char two = ' ';
		for(int i=0; i<NUM_OF_LETTERS; i++)
		{
			if((char)('a'+i)!=one)
			{
				if(lettercount[i]>high)
				{
					high = lettercount[i];
					two = (char)('a'+i);
				}
			}
		}
		
		high=-1;
		char three = ' ';
		for(int i=0; i<NUM_OF_LETTERS; i++)
		{
			if((char)('a'+i)!=one && (char)('a'+i)!=two)
			{
				if(lettercount[i]>high)
				{
					high = lettercount[i];
					three = (char)('a'+i);
				}
			}
		}
		return "Top three letters: \"" + one + "\",\"" + two + "\",\"" + three + "\"";
	}
	
	public String getUnusedLetters()
	{
		StringBuilder s = new StringBuilder("Letters not used: \"");
		for(int i=0; i<26; i++)
		{
			if(lettercount[i]==0)
			{
				s.append((char)('a'+i) + "\",\"");
			}
		}
		if(s.toString().equals("Letters not used: \""))
		{
			return s.toString().substring(0,s.toString().length()-1) + "<None>";
		}
		return s.toString().substring(0,s.toString().length()-2);
	}
	
	public static void main(String[] args) throws IOException
	{
		Word w = new Word();
		w.open();
		if(w.loadText())
		{
			String sep = System.getProperty("line.separator");
			String pattern = "\",./<>?;':[]{}\\|=-0987654321+_)(*&^%$#@!`~\n\r\t " + sep;
			StringTokenizer st = new StringTokenizer(w.getText(), pattern, true);
			int wordcount=0, lettercount=0, symbolcount=0;
			String currentword = "";
			while(st.hasMoreElements())
			{
				currentword = st.nextToken();
				
				if(pattern.indexOf(currentword)>-1)
				{
					if(" \t\r\n".indexOf(currentword)>-1)
					{
						continue;
					}
					symbolcount++;
				}
				else
				{
					wordcount++;
					lettercount += currentword.length();
					w.addWord(currentword);
					w.addLetters(currentword);
				}
			}
			System.out.println(wordcount + " words");
			System.out.println(lettercount + " letters");
			System.out.println(symbolcount + " symbols");
			w.sort();
			System.out.println(w.getThreeWords());
			System.out.println(w.getThreeLetters());
			System.out.println(w.getUnusedLetters());
		}
		else
		{
			System.err.println("Error: could not read file");
		}
		w.close();
	}	
}
