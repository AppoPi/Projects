#include <iostream>

using namespace std;

//Exercise 1-12 Write a program that prints its input one word per line. (p.21)


int main(int argc, char** argv)
{
	for(int i=1; i<argc; i++)
	{
		cout << argv[i] << endl;
	}
}
