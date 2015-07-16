#include <iostream>
#include <string>

using namespace std;

const int SIZE = 4;

int num = 0;

string s = 
"3\n\
7 4\n\
2 4 6\n\
8 5 9 3";

void triangle(int size, int * array){
	int count = 0;
	string curr = "";
	while(count < s.length()){
		if(isdigit(s.at(count))){
			curr.push_back(s.at(count++));
		} else if (count == s.length()){
			array[count++] = stoi(curr);
			curr = "";
		} else {
			array[count++] = stoi(curr);
			curr = "";
		}
	}
}

void initArray(int array[][SIZE], int array2[10]){
	for(int i = 0; i <= num; i++){
		for(int j = 0; j <= num; j++){
			array[i][j] = array2[num];
		}
	}	
}

void fillArray(string t, int * array){
	int n = 1;
	for(int i = 0; i < t.length(); i++){
		if (isdigit(t.at(i))){
			n * 10 + (int)(t.at(i));
		}
		
	}	
}

int main(){
	int array[SIZE][SIZE] = {0};
	int array2[10] = {5,2,5,3,1,5,2,3,1,4};
	
	initArray(array, array2);
	
	for(int i = 0; i < SIZE; i++){
		for(int j = 0; j < SIZE; j++)	{
			cout << array[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}