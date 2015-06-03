#include <iostream>

using namespace std;

bool isPrime(int n){
	if (n <= 1){
		return false;
	} else if (n <= 3){
		return true;
	} else if (n % 2 == 0 || n % 3 == 0){
		return false;
	}
	
	for(int i = 5; i * i <= n; i += 6){
		if (n % i == 0 || n % (i + 2) == 0) {
			return false;
		}
	}
	return true;
}

int nthPrime(int n){
	int count = 0;
	for(int i = 0; count != n; i++){
		if (isPrime(i))
			count++;
			if (count == n)
				return i;
	}
}

int main(){
	cout << nthPrime(10001);
}