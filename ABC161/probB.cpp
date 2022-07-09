#include <iostream>
#include <vector>

int main()
{
    int N, M;
    std::cin >> N >> M;
    std::vector<double> A(N);
    double total = 0;
    for (int i; i < N; i++)
    {
        std::cin >> A.at(i);
        total += A[i];
    }
    double standard = total / (4 * M);
    int ans = 0;
    for (double element : A)
    {
        if (element >= standard)
        {
            ans++;
        }
    }

    if (ans >= M)
    {
        std::cout << "Yes";
    }
    else
    {
        std::cout << "No";
    }
}