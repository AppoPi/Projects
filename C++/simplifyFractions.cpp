#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

#include<boost/tokenizer.hpp>

using namespace std;
using namespace boost;

void simplify(string s){
    tokenizer<> tok(s);
    for(tokenizer<>::iterator beg=tok.begin(); beg!=tok.end(); ++beg){
        *beg;
    }
}

int main(){
    simplify("The quick brown fox jumps over the lazy dog");
}