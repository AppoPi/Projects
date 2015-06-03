#include <iostream>

using namespace std;

int main(){
	for(int i = 2250;; i+=2){
		for(int j = 20; j > 1; j--){
			if (i % j != 0)
				break;
			else if (i % j == 0 && j == 2){
				cout << i << endl;
				return 0;
			}
		}
	}
	return 0;
}