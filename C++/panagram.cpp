#include <iostream>
#include <string>

using namespace std;

string tolower(string s)
{
	string news;

	for(int i = 0; i < s.length(); i++)
	{
		news.push_back((s[i] >= 'A' && s[i] < 'Z') ? s[i] + ('a' - 'A') : s[i]);
	}
	return news;
}

bool isPanagram(string str)
{	
	string s = tolower(str);
	string alphabet = "abcdefghijklmnopqrstuvwxyz";

	for(int i = 0; i < alphabet.length(); i++)
	{
		int index = s.find(alphabet[i]);

		if((index < 0) || (index > s.length()))
		{
			return false;
		}
	}
	return true;
}


//True==1
int main()
{

	string input;
	cout << "Enter some text input: ";
	getline(cin, input);
	cout << "\"" << input  << "\" ";
	string output = (isPanagram(input)) ? "is a panagram\n" : "is not a panagram\n";
	
	cout << output;

	return 0;
}
