#include <iostream>
using namespace std;

string addOne(string str) { 
  string newstr;
  for(int i = 0; i < str.length(); i++){
    if(isalpha(str[i])){
      if(str[i] == 'z'){
		newstr.push_back('a');
      } else if (str[i] == 'Z'){
        newstr.push_back('A');
      } else {
      	newstr.push_back(str[i] + 1 );
      }
    } else {
      newstr.push_back(str[i]);
    }
  }
  return newstr;         
}

string capVowels(string str){
	string newstr;
	string vowels = "aeiou";
	for(int i=0; i < str.length(); i++){
		int f = vowels.find(str[i]);
		if (f != -1){ //found a vowel
			newstr.push_back("AEIOU"[f]);
		} else {
			newstr.push_back(str[i]);
		}
	}
	return newstr;
}

string LetterChanges(string str){
	string newstr = addOne(str);	
	newstr = capVowels(newstr);
	return newstr;
}

int main() { 
  
  // keep this function call here
  cout << LetterChanges(gets(stdin));
  return 0;
    
}           
