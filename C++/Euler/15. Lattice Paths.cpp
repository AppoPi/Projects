#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>

boost::multiprecision::cpp_int factorial(boost::multiprecision::cpp_int n){
	if (n > boost::multiprecision::cpp_int(1))
		return n * factorial(n-boost::multiprecision::cpp_int(1));
	else
		return boost::multiprecision::cpp_int(1);
}

boost::multiprecision::cpp_int cbc(boost::multiprecision::cpp_int n){
	return factorial(boost::multiprecision::cpp_int(2) * n) / (factorial(n) * factorial(n));
}

int main(){
	std::cout << cbc(boost::multiprecision::cpp_int(20)) << std::endl;
	return 0;
}