#include <iostream>
#include <string>

using namespace std;

bool isPrime(int n){
	if(n <= 1) return false;
	else if (n <= 3) return true;
	else if (n % 2 == 0 || n % 3 == 0) return false;
	
	for(int i = 5; i * i <= n; i += 6){
		if (n % i == 0 || n % (i + 2) == 0)
			return false;
	}
	return true;
}

long long sumPrimes(long long n){
	long long sum = 0;
	for(long long i = 2; i < n; i++){
		if (isPrime(i)){
			sum += i;
		}	
	}
	return sum;
}

int main(){
	cout << sumPrimes(2000000);
}