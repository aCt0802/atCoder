#include <bits/stdc++.h>

int main(){
    long long Q;
    std::cin >> Q;
    std::string query;
    std::multiset<long long> set;
    for (long long i = 0; i < Q; i++)
    {
        std::cin >> query;
        if (query[0] == '1')
        {
            set.insert((long long)query[2]);
        }
        else if (query[0] == '2')
        {
            long long search = (long long)query[2], fix = (long long)query[4];
            long long count = std::min(fix, (long long)set.count(search));
            for (long long j = 0; j < count; j++)
            {
                set.erase(set.find(search));
            }
        }
        else
        {
            long long max = 0;
            long long min = 9223372036854775800;
            for (long long val : set){
                max = std::max(max, val);
                min = std::min(min, val);
            }
            std::cout << max - min << std::endl;
        }
    }
}