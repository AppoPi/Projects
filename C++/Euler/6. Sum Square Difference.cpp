#include <iostream>

using namespace std;

int sumSquare(int i, int j){
	int sum = 0;
	for(int a=i; a<=j; a++){
		sum += a * a;
	}
	return sum;
}

int squareSum(int i, int j){
	int sum = 0;
	for(int a=i; a<=j; a++){
		sum += a;
	}
	return sum * sum;
}


int main(){
	cout << squareSum(1,100) - sumSquare(1,100) << endl;
	return 0;
}