#include <iostream>
#include <regex>
#include <string>
using namespace std;

string regexABCheck(string s) {
	smatch m;
	regex e("a...b|b...a");
	if(regex_search(s, m, e)){
		return "true";
	}
	return "false";
}

string ABCheck(string s) {
  for(int i = 0; i < s.length()-4; i++){
    if(s[i] == 'a' && s[i+4] == 'b')
       return "true";
    else if(str[i] == 'b' && str[i+4] == 'a')
      return "true";
  }
  return "false";
}

int main() {
	string s = "This is a test string. Laura sobs.";
		
	cout << ABCheck(s);
	return 0;
}