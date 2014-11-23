#include <iostream>
#include <fstream>
#include <string>

using namespae std;

int main(){
	string line;
	ifstream f ("wordlist.txt");
	if(f.is_open()){
		while(getline(f,line)){
		cout << line << endl;
		}
		f.close();
	} else cout << "Unable to open file" << endl;
}