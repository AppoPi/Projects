#include <iostream>
using namespace std;

string LetterCapitalize(string str) { 
  string newstr;
  for(int i = 0; i < str.length(); i++){
    if(i==0 || !isalnum(str[i-1])){
      if (str[i] > 96) {
     	newstr.push_back(str[i] - 32);
      } else {
     	newstr.push_back(str[i]);
      }
    } else {
      	newstr.push_back(str[i]);
    }
  }
  return newstr;       
}

int main() { 
  
  // keep this function call here
  cout << LetterCapitalize(gets(stdin));
  return 0;
    
}           
