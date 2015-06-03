#include <iostream>
#include <string>

using namespace std;

int isPalindrome(string c){
	for(int i=0; i < c.length()/2; i ++){
		if (c[i] != c[c.length()-1-i]){
			return 0; // False
		}
	}
	return 1; //True
}

int main(){
	int max = 1;
	for(int i = 111; i < 1000; i++){
		for(int j = 111; j < 1000; j++){
			if (isPalindrome(to_string(i * j))) {
				if (i * j > max){
					 max = i * j;
				}
			}
		}
	}
	cout << max << endl;
	return 0;
}