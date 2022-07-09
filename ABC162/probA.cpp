#include <iostream>
#include <string.h>

int main()
{
    std::string N;
    std::cin >> N;

    if (N[0] == '7' || N[1] == '7' || N[2] == '7')
    {
        std::cout << "Yes";
    }
    else
    {
        std::cout << "No";
    }
}