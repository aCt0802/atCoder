#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> squares;

    int maxNumber = 0;

    int temp;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++){
            cin >> temp;
            squares.at(i).at(j) = temp;
            maxNumber = max(maxNumber, temp);
        }
    }
}