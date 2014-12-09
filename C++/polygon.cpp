#include <iostream>
#include <cmath>
#include <sstream>
#include <stdio.h>

#define _USE_MATH_DEFINE

using namespace std;

double string_to_double( const std::string& s )
{
	std::istringstream i(s);
	double x;
	if (!(i >> x))
		return 0;
	return x;
} 

int main(int argc, char** argv)
{
	if(argc != 3){cout << "Not correct number of arguments. Expected 2.\n"; return 0;}

	double sides = string_to_double(argv[1]);
	double circumradius = string_to_double(argv[2]);

	cout << "SIDES: " << sides << endl;
	cout << "CIRCUMRADIUS: " << circumradius << endl;

	double length = circumradius * 2 * sin(M_PI / sides);

	printf("%4.3f\n", sides*length);
	return 0;
}
