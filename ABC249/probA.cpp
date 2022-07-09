#include<iostream>

int main(){
    int A, B, C, D, E, F, X;
    std::cin >> A >> B >> C >> D >> E >> F >> X;
    int takahashi = (B * A) * (X / (A + C));
    if(X % (A + C) <= A){
        takahashi += (X % (A + C)) * B;
    }else{
        takahashi += A * B;
    }

    int aoki = (D * E) * (X / (D + F));
    if(X % (D + F) <= D){
        aoki += (X % (D + F)) * E;
    }else{
        aoki += D * E;
    }

    // std::cout << aoki << std::endl << takahashi;

    if (takahashi < aoki){
        std::cout << "Aoki";
    }else if (takahashi > aoki)
    {
        std::cout << "Takahashi";
    }else{
        std::cout << "Draw";
    }
    
    
}