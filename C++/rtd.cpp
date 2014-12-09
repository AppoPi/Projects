#include <iostream>
#include <stdlib.h>
#include <ctime>

using namespace std;

int main(int argc, char** argv)
{
	string i = argv[1],
	r = i.substr(0,i.find("d",0)),
	s = i.substr(i.find("d",0)+1, i.length());

	int rolls = atoi(r.c_str()),
	sides = atoi(s.c_str());
	srand (time(0));

	for(int i = 0; i < rolls; i++)
	{
		cout <<  (rand() % sides + 1) << " ";
	}
	cout << endl;
}	
