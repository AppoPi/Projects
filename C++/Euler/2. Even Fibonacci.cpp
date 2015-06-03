#include <iostream>
using namespace std;

int main(){
	int one = 1;
	int two = 2;
	int sum = 2;
	
	while(sum <= 4000000){
		int temp = one;
		one = two;
		two += temp;
		if (two % 2 == 0)
			sum += two;
	}
	cout << sum << endl;
}