#include<iostream>
#include<vector>

int main(){
    int N, X;
    std::cin >> N >> X;
    std::vector<std::vector<int>> nums(N, std::vector<int>(2));
    for (int i = 0; i < N; i++)
    {
        std::cin >> nums.at(i).at(0) >> nums.at(i).at(1);
    }
    std::vector<long long>dp(N);

    for (int i = 0; i < N; i++){
        
    }
}