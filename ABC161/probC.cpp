#include <iostream>
#include <vector>
#include <algorithm>

//https://atcoder.jp/contests/abc161/tasks/abc161_c

int main(){
    long long N, K;
    std::cin >> N >> K; 
    N %= K;
    long long assumed = std::abs(N - K);
    std::cout << std::min(N, assumed);
}

int wrong_main()
{
    long long N, K;
    std::cin >> N >> K;
    std::vector<long long> results(1);
    results[0] = N;
    if (K != 1)
    {
        if ((N % 2 == 0 && K % 2 == 0) || (N % 2 == 1 && K % 2 == 1))
        {
            while (true)
            {
                N = std::abs(N - K);
                auto elemIter = std::find(results.begin(), results.end(), N);
                if (elemIter == results.end())
                {
                    std::cout << *std::min_element(results.begin(), results.end());
                    break;
                }
                else
                {
                    results.push_back(N);
                }
            }
        }
        else
        {
            std::cout << 1;
        }
    }
    else
    {
        std::cout << 0;
    }
}