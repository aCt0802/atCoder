#include <bits/stdc++.h>

using namespace std;

int main()
{
    int time, min;
    cin >> min;
    if (min / 60 >= 1)
    {
        time = 22;
        min %= 60;
    }
    else
    {
        time = 21;
    }
    string ans;
    if (min < 10)
    {
        cout << time << ":0" << min;
    }
    else
    {
        cout << time << ":" << min;
    }
}