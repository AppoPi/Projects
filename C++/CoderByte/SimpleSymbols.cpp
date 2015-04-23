#include <iostream>
using namespace std;

string SimpleSymbols(string str) { 
	for (int i = 0; i < str.length(); i++){
		if (isalpha(str[i])) {
			if (str[i-1] != '+' || str[i+1] != '+') {
				return "false";
			}
		}
	}
	return "true";
}

int main() { 
  
  // keep this function call here
  cout << SimpleSymbols(gets(stdin));
  return 0;
    
}          