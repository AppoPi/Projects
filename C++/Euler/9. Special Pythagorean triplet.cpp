#include <iostream>
#include <math.h>
using namespace std;

int addends(int sum){
	for(int a = 2; a < sum; a++){
		for(int b = a + 1; b < sum; b++){
			int c = 1000 - a - b;
			if (a * a + b * b == c * c){
				//cout << a << endl << b << endl << c << endl;
				return a * b * c;
			}
		}
	}
	return -1;
}

int main(){
	cout << addends(1000);
}