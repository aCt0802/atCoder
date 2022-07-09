#include <iostream>
#include <vector>
#include <string>

int main()
{
    std::vector<int> nums(10);
    for (int i = 0; i < 10; i++)
    {
        std::cin >> nums.at(i);
    }
    std::cout << nums[nums[nums[0]]];
}
