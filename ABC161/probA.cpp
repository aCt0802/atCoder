#include<iostream>

int main(){
    int A, B, C;
    std::cin>> A >> B >> C;
    std::swap(A, B);
    std::swap(A, C);
    std::cout << A << ' ' << B << ' ' << C;
}