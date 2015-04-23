#include <iostream>
using namespace std;

int FirstFactorial(int num) { 
  // code goes here
  int p = 1;
  for(int i=num; i > 0; i--){
    p *= i;
  }
  return p;
}

int main() {
  // keep this function call here
  cout << FirstFactorial(gets(stdin));
  return 0;
}           
