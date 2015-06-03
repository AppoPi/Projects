#include <iostream>
#include <vector>

using namespace std;


long long collatz(long long n){
	return   (n % 2 == 0) ? (n / 2) : (3 * n + 1);
}

int main(){
	//Range 2 - 1,000,000
	const int START = 2;
	const int SIZE = 1000000;
	//Use a vector to store already calculated collatz's
	vector<long long> numbers(SIZE, 0);
	
	long long count = 1, max_num = 1, max_count = -1;
	for(int i=START; i < SIZE; i++){
		long long n = i;
		while (n > 1){
			//Calculate next number in sequence
			n = collatz(n);
			
			if (n < i && numbers.at(n) != 0){
				//If already calculated collatz of number add current count with number count
				count += numbers.at(n);
				break;
			}
			
			count++;
		}
		//If in the array range, store it
		if (i < SIZE && i > 0)
			numbers[i] = count;
		//If a new highest count is find, record it
		if (count > max_count){
			max_count = count;
			max_num = i;
		}
		//Print numbers and their collatz steps to 1
		//cout << i << ": " << count << endl;

		//Reset count
		count = 1;
	}
	//Print highest collatz number and value
	cout << max_num << " " << max_count << endl;

	return 0;
}

