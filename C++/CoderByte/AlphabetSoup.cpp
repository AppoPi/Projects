#include <iostream>
using namespace std;

string swap(string &str, int pos1, int pos2) {
	char c = str[pos2];
	str[pos2] = str[pos1];
	str[pos1] = c;
	return str;
}

string AlphabetSoup(string str) { 
	for (int j=0; j < str.length(); j ++){
		for (int i = 0; i < str.length() -1  - j; i++){
			if(str[i] > str[i+1]) {
				swap(str, i, i+1);
			}
		}
	}
  return str;      
}

int main() { 
  cout << AlphabetSoup(gets(stdin));
  return 0;  
} 
