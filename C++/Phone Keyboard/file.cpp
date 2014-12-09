// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>

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

void printDict()
{
	for(int i=0; i<LINES; i++)
	{
		cout << dict[i] << endl;
	}
	return;
}

void lookup(char* word)
{
	string str(word);

	for(int i=0; i<LINES; i++)
	{
		if(str == dict[i].substr(0,str.length()))
		{
			cout << dict[i] << endl;
		}
	}
}

int main ()
{
	char * filename = "lower.txt";
	loadDict(filename);
	string input;
	cout << "Enter a keyword: ";
	cin >> input;
	char* c = new char[input.size()+1];
	c[input.size()] = '\0';
	memcpy(c, input.c_str(), input.size());

	lookup(c);

	return 0;
}
