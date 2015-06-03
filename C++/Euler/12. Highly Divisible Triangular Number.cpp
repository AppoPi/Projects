#include <iostream>
#include <cmath>

using namespace std;

long long add = 0;
long long Triangle(){
	add++;
	return add * (add + 1) / 2;
}

int countDivisors(long long n){
	int count = 0;
	float s = sqrt((float)n);
	for(long long i=1; i <=n; i++){
		if (n % i == 0)
			count++;
		if((float)i == s){
			return 2 * count - 1;
		} else if ((float)i > s){
			return 2 * count;
		}
	}
	return count;
}


int main(){
	long long n = 1;
	int c = 0;
	
	do {
		n = Triangle();
		c = countDivisors(n);
	} while(c <= 500);
	cout << n << endl;
	return 0;
}