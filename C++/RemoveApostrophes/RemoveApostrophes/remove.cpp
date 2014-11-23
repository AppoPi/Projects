// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>

using namespace std;

int main () {
	vector<string> list;
	vector<string> trimmed;

	string line;
	ifstream input;
	input.open ("wordlist.txt");


	//string pattern = "[A-Z][A-Za-z']+|([A-Za-z]+?'s)";
	//string text = "test\none\ntwo\nthree";


	int i = 0;

	if (input.is_open()){
		while ( getline (input, line)){
			list.push_back(line);
			i++;
		}
		input.close();
	}

	string cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string s;
	for(int i=0; i<list.size(); i++){
		s = list.at(i);
		//Has an apostrophe or starts with a capital letter
		if (s.find("'") == -1 && cap.find(s.at(0)) == -1){
			trimmed.push_back(s);
		}
	}

	ofstream output;
	output.open ("formmatted.txt");

	for (int i=0; i < trimmed.size(); i++){
		output << trimmed.at(i) << endl;
	}

	output.close();

	return 0;
}