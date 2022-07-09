#include <iostream>
#include <vector>
#include <numeric>

int main()
{
    long long ans = 0;

    int N;
    std::cin >> N;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            for (int k = 1; k <= N; k++)
            {
                ans += std::gcd(std::gcd(i, j), k);
            }
        }
    }

    std::cout << ans;
}