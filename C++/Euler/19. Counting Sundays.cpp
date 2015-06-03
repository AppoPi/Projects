#include <iostream>
#include <string>

using namespace std;

bool isLeapYear(int year){
	if (year % 4 != 0) return false;
	else if (year % 100 != 0) return true;
	else if (year % 400 != 0) return false;
	else return true;
}

string isSunday(int month, int year){
	int m[12] = { 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5};
	int c = 0;
	if (year % 4 == 0) c = 6;
	else if (year % 4 == 1) c = 4;
	else if (year % 4 == 2) c = 2;
	else if (year % 4 == 3) c = 0;
	if (isLeapYear(year))
		return ((1 + m[month] + year + year/4 + c) % 7 == 0) ? "true" : "false";
}


int main(){
	int count = 0;
	for(int j = 1901; j < 2001; j++)
		for(int i = 0; i < 12; i ++)
			if (isSunday(i, j)=="true"){
				cout << i << "-" << j << endl;
				count ++;
			}
	
	cout << count << endl;
	return 0;
}