#include<bits/stdc++.h>

int get_min(std::vector<int> vec){
    int min = vec[0];
    for(int elem : vec){
        if(elem < min){
            min = elem;
        }
    }
    return min;
}

int get_max(std::vector<int> vec){
    int max = vec[0];
    for(int elem : vec){
        if(elem > max){
            max = elem;
        }
    }
    return max;
}

int main(){
    int N;
    std::string S;
    std::cin >> N >> S;
    std::vector<int> W(N);
    for(int i = 0; i < N ; i++){
        std::cin >> W[i];
    }
    int search = get_min(W);
    int maxW = get_max(W) + 2;

    int count;
    int ans = 0;

    char assume;

    while (search <= maxW)
    {
        count = 0;
        for(int i = 0; i < N; i++){
            if(W[i] >= search){
                assume = '1';
            }else{
                assume = '0';
            }
            if(assume == S[i]){
                count++;
            }
        }
        ans = std::max(count, ans);
        // double minus = search - 0.1;
        // count = 0;
        // for(int i = 0; i < N; i++){
        //     if(W[i] >= minus){
        //         assume = '1';
        //     }else{
        //         assume = '0';
        //     }
        //     if(assume == S[i]){
        //         count++;
        //     }
        // }
        // ans = std::max(count, ans);
        // double plus = search + 0.1;
        // count = 0;
        // for(int i = 0; i < N; i++){
        //     if(W[i] >= plus){
        //         assume = '1';
        //     }else{
        //         assume = '0';
        //     }
        //     if(assume == S[i]){
        //         count++;
        //     }
        // }
        // ans = std::max(count, ans);

        search++;
    }

    std::cout << ans;
    
}