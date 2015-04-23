#include <iostream>
#include <sstream>
using namespace std;

string TimeConvert(int num) {
  string ret;
  std::stringstream ss;
  ss << num / 60;
  ss << ":";
  ss  <<num % 60; 
  return ss.str();
}

int main() { 
  cout << TimeConvert(gets(stdin));
  return 0;
    
} 
