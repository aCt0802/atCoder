#include <bits/stdc++.h>

int main()
{
    int h1, h2, h3, w1, w2, w3;
    std::cin >> h1 >> h2 >> h3 >> w1 >> w2 >> w3;
    std::vector<std::vector<int>> wv1, wv2, wv3;

    for (int i = 1; i <= h1 - 2; i++)
    {
        for (int j = 1; j <= h1 - 2; j++)
        {
            for (int k = 1; k <= h1 - 2; k++)
            {
                if (i + j + k == h1)
                {
                    wv1.push_back({i, j, k});
                }
            }
        }
    }
    for (int i = 1; i <= h2 - 2; i++)
    {
        for (int j = 1; j <= h2 - 2; j++)
        {
            for (int k = 1; k <= h2 - 2; k++)
            {
                if (i + j + k == h2)
                {
                    wv2.push_back({i, j, k});
                }
            }
        }
    }
    for (int i = 1; i <= h3 - 2; i++)
    {
        for (int j = 1; j <= h3 - 2; j++)
        {
            for (int k = 1; k <= h3 - 2; k++)
            {
                if (i + j + k == h3)
                {
                    wv3.push_back({i, j, k});
                }
            }
        }
    }

    // std::cout << vv[1][0] << vv[1][1] << vv[1][2];

    int ans, wSum1, wSum2, wSum3;
    ans = 0;

    for (std::vector<int> vElem1 : wv1)
    {
        for (std::vector<int> vElem2 : wv2)
        {
            for (std::vector<int> vElem3 : wv3)
            {
                wSum1 = vElem1[0] + vElem2[0] + vElem3[0];
                wSum2 = vElem1[1] + vElem2[1] + vElem3[1];
                wSum3 = vElem1[2] + vElem2[2] + vElem3[2];
                // std::cout << "wSum1 : " << wSum1 << std::endl;
                // std::cout << "wSum2 : " << wSum2 << std::endl;
                // std::cout << "wSum3 : " << wSum3 << std::endl;
                if (wSum1 == w1 && wSum2 == w2 && wSum3 == w3){
                    ans++;
                }
            }
        }
    }

    std::cout << ans;
}