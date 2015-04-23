#include <iostream>
#include <string>

using namespace std;

int count(string s){
	int c = 0;
	for(int i = 0; i < s.length(); i++){
		switch(s[i]) {
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u':
			case 'A':
			case 'E':
			case 'I':
			case 'O':
			case 'U':
				c++;
		}
	}
	return c;
}



int main() {
		
	cout << count(gets(stdin));
	return 0;
}

main.cpp: In function 'std::string WordCount(std::string)':main.cpp:12:10: error: invalid conversion from 'int' to 'const char*' [-fpermissive]   return count;          ^In file included from /usr/include/c++/4.8/string:53:0,                 from /usr/include/c++/4.8/bits/locale_classes.h:40,                 from /usr/include/c++/4.8/bits/ios_base.h:41,                 from /usr/include/c++/4.8/ios:42,                 from /usr/include/c++/4.8/ostream:38,                 from /usr/include/c++/4.8/iostream:39,                 from main.cpp:1:/usr/include/c++/4.8/bits/basic_string.tcc:212:5: error:   initializing argument 1 of 'std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const _CharT*, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]' [-fpermissive]     basic_string<_CharT, _Traits, _Alloc>::     ^