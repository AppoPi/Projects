#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

cpp_int sumDigits(cpp_int i){
	cpp_int sum = 0;
	while( i > cpp_int(0)){
		sum += i % cpp_int(10);
		i /= cpp_int(10);
	}
	return sum;
}

cpp_int pow(cpp_int i, int p){
	if (p == 0){
		return cpp_int(1);
	}
	else if (p > 0){
		cpp_int r = i;
		for(int a=1; a < p; a++){
			r *= i;
		}
		return r;
	} else {
		return -1;
	}
}

int main(){
	cout << sumDigits(pow(cpp_int(2), 1000)) << endl;
	return 0;
}