#include <iostream>
using namespace std;

string LongestWord(string sen) {
  // code goes here
  int maxLength = 0;
  string maxWord = "";
  string * array = new string[100];
  string word = "";
  for(int i = 0; i < sen.length(); i++){
    if(isalpha(sen[i]) || isdigit(sen[i])){
       word.push_back(sen[i]);
    }
    if(i==sen.length()-1 //Arrived at last char
    || !isalnum(sen[i])){ //Arrived at end of word
    	if (word.length() > maxLength){
    		maxLength = word.length();
    		maxWord = word;
    	}
	    word.clear();
    }
  }
  return maxWord;
}

int main() { 
  
  // keep this function call here
  cout << LongestWord(gets(stdin));
  return 0;
    
}           
