#include <iostream>
#include <vector>

int main()
{
    int N;
    std::cin >> N;

    long long count = 0;

    for (int i = 1; i <= N; i++)
    {
        if (i % 3 != 0 && i % 5 != 0)
        {
            count += i;
        }
    }

    std::cout << count;
}