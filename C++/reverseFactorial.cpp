#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string factorial(int n){
    int num = n;
    for(int i=2; i<n; i++){
        if (num % i == 0){
            // cout << n << " is divisible by " << i << endl;
            num /= i;
            if (num == 1){
                ostringstream ss;
                ss << i;
                return ss.str() + "!";
            }
        }       
    }
    return "NONE";
}

int main(){
    cout << factorial(120) << endl;
    cout << factorial(150) << endl;
    cout << factorial(3628800) << endl;
    cout << factorial(479001600) << endl;
    cout << factorial(6) << endl;
    cout << factorial(18) << endl;
}