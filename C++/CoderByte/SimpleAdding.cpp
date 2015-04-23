#include <iostream>
using namespace std;

int SimpleAdding(int num) {
  int sum = 0;
  for (int i = 0; i <= num; i++){
    sum += i;
  }
  // code goes here   
  return sum; 

}

int main() { 
  
  // keep this function call here
  cout << SimpleAdding(gets(stdin));
  return 0;
    
}           
