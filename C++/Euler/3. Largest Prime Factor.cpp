#include <iostream>

using namespace std;

int largestPrime(long long x){
	int counter = 2; //Initialize counter
	while(x > 0 && counter < x) { //Loop
		if (x % counter == 0) { //Is divisible
			x /= counter; //Divide by prime
			counter = 2; //Reset counter
		 } else {
			counter++; //Increment counter
		}
	}
	return counter;
}

int main(){
	cout << "The largest prime factor is " <<
		largestPrime(600851475143);
}
