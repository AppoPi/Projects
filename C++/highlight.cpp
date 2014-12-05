#include <iostream>
#include <sstream>
#include <string>
#include <locale>


using namespace std;

/**  
    Converts string to lowercase regardless of character set
    assuming the characterset has a contiguous A-Z and a-z
    and a-z is after A-Z
  */
string tolower(string s)
{
	string news;

	for(int i=0; i<s.length(); i++)
	{
		news.push_back((s[i]>='A' && s[i] <'Z') ? s[i]+('a'-'A') : s[i]);
	}
	return news;
}

int main ()
{
	//Prompt user for input
	cout << "Enter some text: ";
	string input;
	getline(cin, input);

	//Initialize Periodic Table
	string periodic[118] =
	{
		"H","He","Li","Be","B","C","N","O",
		"F","Ne","Na","Mg","Al","Si","P","S",
		"Cl","Ar","K","Ca","Sc","Ti","V","Cr",
		"Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge",
		"As","Se","Br","Kr","Rb","Sr","Y","Zr",
		"Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd",
		"In","Sn","Sb","Te","I","Xe","Cs","Ba",
		"Lu","Hf","Ta","W","Re","Os","Ir","Pt",
		"Au","Hg","Tl","Pb","Bi","Po","At","Rn",
		"Fr","Ra","Lr","Rf","Db","Sg","Bh","Hs",
		"Mt","Ds","Rg","Cn","Uut","Fl","Uup","Lv",
		"Uus","Uuo","La","Ce","Pr","Nd","Pm","Sm",
		"Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",
		"Ac","Th","Pa","U","Np","Pu","Am","Cm",
		"Bk","Cf","Es","Fm","Md","No"
	};

	//Loop Through Text
	for(int i = 0; i < input.length(); i++)
	{
		//Loop Through Elements
		for(int j = 0; j < sizeof(periodic)/sizeof(periodic[j]); j++)
		{
			if(tolower(input).substr(i, periodic[j].length()) == tolower(periodic[j]))
			{
				//Format output with brackets and properly capitalized element symbol
				stringstream ss;
				ss << "[" << periodic[j] << "]";
				string s = ss.str();
				//Print out matches as soon as they are found
				cout << input.substr(0,i) << s <<
					input.substr(i+periodic[j].length(),
					input.length()) << endl;
			}
		}
	}

}
