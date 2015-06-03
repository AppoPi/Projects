#include <iostream>
#include <string>

using namespace std;

string written(int i){
	if (i < 0)			return "negative " + written(i * -1);
	else if (i == 0)	return "zero ";
	else if (i == 1)	return "one ";
	else if (i == 2)	return "two ";
	else if (i == 3)	return "three ";
	else if (i == 4)	return "four ";
	else if (i == 5)	return "five ";
	else if (i == 6)	return "six ";
	else if (i == 7)	return "seven ";
	else if (i == 8)	return "eight ";
	else if (i == 9)	return "nine ";
	else if (i == 10)	return "ten ";
	else if (i == 11)	return "eleven ";
	else if (i == 12)	return "twelve ";
	else if (i == 13)	return "thirteen ";
	else if (i == 14)	return "fourteen ";
	else if (i == 15)	return "fifteen ";
	else if (i == 16)	return "sixteen ";
	else if (i == 17)	return "seventeen ";
	else if (i == 18)	return "eighteen ";
	else if (i == 19)	return "nineteen ";
	else if (i == 20)	return "twenty ";
	else if (i < 30)	return "twenty-" + written(i % 10);
	else if (i == 30)	return "thirty ";
	else if (i < 40)	return "thirty-" + written(i % 10);
	else if (i == 40)	return "forty ";
	else if (i < 50)	return "forty-" + written(i % 10);
	else if (i == 50)	return "fifty ";
	else if (i < 60)	return "fifty-" + written(i % 10);
	else if (i == 60)	return "sixty ";
	else if (i < 70)	return "sixty-" + written(i % 10);
	else if (i == 70)	return "seventy ";
	else if (i < 80)	return "seventy-" + written(i % 10);
	else if (i == 80)	return "eighty ";
	else if (i < 90)	return "eighty-" + written(i % 10);
	else if (i == 90)	return "ninety ";
	else if (i < 100)	return "ninety-" + written(i % 10);
	else if (i == 100)	return "one hundred";
	else if (i < 200)	return "one hundred and " + written(i % 100);
	else if (i == 200)	return "two hundred";
	else if (i < 300)	return "two hundred and " + written(i % 100);
	else if (i == 300)	return "three hundred";
	else if (i < 400)	return "three hundred and " + written(i % 100);
	else if (i == 400)	return "four hundred";
	else if (i < 500)	return "four hundred and " + written(i % 100);
	else if (i == 500)	return "five hundred";
	else if (i < 600)	return "five hundred and " + written(i % 100);
	else if (i == 600)	return "six hundred";
	else if (i < 700)	return "six hundred and " + written(i % 100);
	else if (i == 700)	return "seven hundred";
	else if (i < 800)	return "seven hundred and " + written(i % 100);
	else if (i == 800)	return "eight hundred";
	else if (i < 900)	return "eight hundred and " + written(i % 100);
	else if (i == 900)	return "nine hundred";
	else if (i < 1000)	return "nine hundred and " + written(i % 100);
	else if (i == 1000)	return "one thousand";

	else return "VALUE OUTSIDE OF VALID RANGE";
}

int countLetters(string s){
	int count = 0;
	for(unsigned int i = 0; i < s.length(); i++){
		if(isalpha(s.at(i))){
			count++;
		}
	}
	return count;
}

int main(){
	int a = 1000, sum = 0;
	for(int i= 1; i <= a; i++){
		sum += countLetters(written(i));
	}
	cout << sum << endl;
	return 0;
}