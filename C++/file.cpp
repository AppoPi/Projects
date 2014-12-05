#include <iostream>
#include <fstream>
#include <string>

using namespace std;


string * dict;
int LINES;

int countLines(char* filename)
{
	string line;
	ifstream myfile (filename);
	int count = 0;
	if (myfile.is_open())
	{
		while ( getline (myfile,line) )
		{
			count++;
		}
		myfile.close();
	}
	else
	{
		cout << "Unable to open file"; 
	}
	myfile.close();
	return count;
}

void loadDict(char* filename)
{
	ifstream myfile (filename);
	LINES = countLines(filename);
	dict = new string[LINES];
	string line;
	int i = 0;
	while(getline(myfile, line))
	{
		dict[i++] = line;
	}

	myfile.close();
	return;
}

void lookup(string str)
{
	for(int i=0; i<LINES; i++)
	{
		//contains
		//if(dict[i].find(str) >= 0 && dict[i].find(str) < dict[i].length())
		//starts with
		if(dict[i].substr(0, str.length()) == str)
		{
			cout << dict[i] << endl;
		}
	}
}

string convert(string s)
{
	s.push_back(' ');
	int changed = 1;
	while(changed != 0)
	{
		changed = 0;
		try
		{
			if(s.length()>4)
			{
				if(s.find("7777 ", 0) >= 0 && s.find("7777 ", 0) < s.length())
				{
					s.replace(s.find("7777 "), 5, "s");
					changed = 1;
				}
				else if(s.find("9999 ", 0) >= 0 && s.find("9999 ", 0) < s.length())
				{
					s.replace(s.find("9999 "), 5, "z");
					changed = 1;
				}
			}
		}
		catch(int x)
		{
			cout << " Error four" << endl;
		}
	}
	
	changed = 1;
	while(changed != 0)
	{
		changed = 0;
		try
		{
			if(s.length()>3)
			{
				if(s.find("222 ") >= 0 && s.find("222 ") < s.length())
				{
					s.replace(s.find("222 ", 0), 4, "c");
					changed = 1;
				}
				else if(s.find("333 ", 0) >= 0 && s.find("333 ", 0) < s.length())
				{
					s.replace(s.find("333 "), 4, "f");
					changed = 1;
				}
				else if(s.find("444 ", 0) >= 0 && s.find("444 ", 0) < s.length())
				{
					s.replace(s.find("444 "), 4, "i");
					changed = 1;
				}
				else if(s.find("555 ", 0) >= 0 && s.find("555 ", 0) < s.length())
				{
					s.replace(s.find("555 "), 4, "l");
					changed = 1;
				}
				else if(s.find("666 ", 0) >= 0 && s.find("666 ", 0) < s.length())
				{
					s.replace(s.find("666 "), 4, "o");
					changed = 1;
				}
				else if(s.find("777 ", 0) >= 0 && s.find("777 ", 0) < s.length())
				{
					s.replace(s.find("777 "), 4, "r");
					changed = 1;
				}
				else if(s.find("888 ", 0) >= 0 && s.find("888 ", 0) < s.length())
				{
					s.replace(s.find("888 "), 4, "v");
					changed = 1;
				}
				else if(s.find("999 ", 0) >= 0 && s.find("999 ", 0) < s.length())
				{
					s.replace(s.find("999 "), 4, "y");
					changed = 1;
				}
			}
		}
		catch(int x)
		{
			cout << " Error three " << endl;
		}
	}

	changed = 1;
	while(changed!=0)
	{
		changed = 0;
		try
		{
			if(s.length()>2)
			{
				if(s.find("22 ", 0) >= 0 && s.find("22 ", 0) < s.length())
				{
					s.replace(s.find("22 "), 3, "b");
					changed = 1;
				}
				else if(s.find("33 ", 0) >= 0 && s.find("33 ", 0) < s.length())
				{
					s.replace(s.find("33 "), 3, "e");
					changed = 1;
				}
				else if(s.find("44 ", 0) >= 0 && s.find("44 ", 0) < s.length())
				{
					s.replace(s.find("44 "), 3, "h");
					changed = 1;
				}
				else if(s.find("55 ", 0) >= 0 && s.find("55 ", 0) < s.length())
				{
					s.replace(s.find("55 "), 3, "k");
					changed = 1;
				}
				else if(s.find("66 ", 0) >= 0 && s.find("66 ", 0) < s.length())
				{
					s.replace(s.find("66 "), 3, "n");
					changed = 1;
				}
				else if(s.find("77 ", 0) >= 0 && s.find("77 ", 0) < s.length())
				{
					s.replace(s.find("77 "), 3, "q");
					changed = 1;
				}
				else if(s.find("88 ", 0) >= 0 && s.find("88 ", 0) < s.length())
				{
					s.replace(s.find("88 "), 3, "u");
					changed = 1;
				}
				else if(s.find("99 ", 0) >= 0 && s.find("99 ", 0) < s.length())
				{
					s.replace(s.find("99 "), 3, "x");
					changed = 1;
				}
			}
		}
		catch(int x)
		{
			cout << " Error two " << endl;
		}
	}

	changed = 1;
	while(changed!=0)
	{
		changed = 0;
		try
		{
			if(s.length()>1)
			{
				if(s.find("2 ", 0) >= 0 && s.find("2 ", 0) < s.length())
				{
					s.replace(s.find("2 "), 2, "a");
					changed = 1;
				}
				else if(s.find("3 ", 0) >= 0 && s.find("3 ", 0) < s.length())
				{
					s.replace(s.find("3 "), 2, "d");
					changed = 1;
				}
				else if(s.find("4 ", 0) >= 0 && s.find("4 ", 0) < s.length())
				{
					s.replace(s.find("4 "), 2, "g");
					changed = 1;
				}
				else if(s.find("5 ", 0) >= 0 && s.find("5 ", 0) < s.length())
				{
					s.replace(s.find("5 "), 2, "j");
					changed = 1;
				}
				else if(s.find("6 ", 0) >= 0 && s.find("6 ", 0) < s.length())
				{
					s.replace(s.find("6 "), 2, "m");
					changed = 1;
				}
				else if(s.find("7 ", 0) >= 0 && s.find("7 ", 0) < s.length())
				{
					s.replace(s.find("7 "), 2, "p");
					changed = 1;
				}
				else if(s.find("8 ", 0) >= 0 && s.find("8 ", 0) < s.length())
				{
					s.replace(s.find("8 "), 2, "t");
					changed = 1;
				}
				else if(s.find("9 ", 0) >= 0 && s.find("9 ", 0)< s.length())
				{
					s.replace(s.find("9 "), 2, "w");
					changed = 1;
				}
			}
		}
		catch(int x)
		{
			cout << " Error one " << endl;
		}
	}
	return s;
}

int main()
{
/* EXAMPLES
7777 666 555 3
7 33 2 222 44 999
55 33 33 66
*/
	char * filename = "lower.txt";
	loadDict(filename);

	string input;
	cout << "Enter keyboard sequence: ";
	getline(cin,input);

	lookup(convert(input));

	return 0;
}
