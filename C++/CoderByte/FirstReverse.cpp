#include <iostream>
using namespace std;

string FirstReverse(string str) { 
  // code goes here
  string newstring;
  for(int i=0; i < str.length(); i++){
	 //newstr.push_back(str[str.length() - i]);
    newstring.push_back(str[str.length()-i-1]);
  }
  return newstring; 
}


int main() { 
  
  // keep this function call here
  cout << FirstReverse(gets(stdin));
  return 0;
    
}      