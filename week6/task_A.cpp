#include <iostream>
#include <deque>
 
 
std::string grasshopper(int n, int k, int *arr) {
    int dp[n + 1];
    int coins[n + 1];
 
    dp[1] = 0;
    int nmax = 0;
    for (int i = 2; i <= n; ++i) {
        nmax = i - 1;
        int max = (i - k) > 1 ? i - k : 1;
        for (int j = max; j < i; ++j) {
            if (dp[nmax] < dp[j]) {
                nmax = j;
            }
        }
        coins[i] = nmax;
        dp[i] = dp[nmax] + arr[i];
    }
 
    int cnt = 0;
    int num = n;
    std::deque<int> jumps;
    jumps.push_back(num);
    while (num > 1) {
        num = coins[num];
        jumps.push_back(num);
        cnt++;
    }
 
    std::string output = std::to_string(dp[n]) + "\n" + std::to_string(cnt) + "\n";
 
    while (!jumps.empty()) {
        output += std::to_string(jumps.back()) + " ";
        jumps.pop_back();
    }
 
    return output;
}
 
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, k;
    std::cin >> n >> k;
    int arr[n + 1];
    arr[1] = 0;
    arr[n] = 0;
    for (int i = 2; i < n; ++i) {
        std::cin >> arr[i];
    }
    std::cout << grasshopper(n, k, arr);
 
    return 0;
}
