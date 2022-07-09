#include <iostream>
#include <vector>
#include <string>

int main()
{
    int N, X;
    std::cin >> N >> X;
    std::vector<std::vector<int>> nums(N, std::vector<int>(2));
    for (int i = 0; i < N; i++)
    {
        std::cin >> nums.at(i).at(0) >> nums.at(i).at(1);
    }

    std::string ans = "No";
    for (int bit = 0; bit < (1 << N); bit++)
    {
        long long sum = 0;
        for (int i = 0; i < N; i++)
        {
            if (bit & (1 << i))
            {
                sum += nums[i][0];
            }
            else
            {
                sum += nums[i][1];
            }
        }

        if (sum == X)
        {
            ans = "Yes";
            break;
        }
    }

    std::cout << ans;
}