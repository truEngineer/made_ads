#include <iostream>
#include <algorithm>
#include <vector>
 
const int W_MAX = 10000;
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> graph;
    graph.resize(n, std::vector<int>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> graph[i][j];
            if (graph[i][j] == 100000) {
                graph[i][j] = INT32_MAX - W_MAX;
            }
        }
    }
    std::vector<int64_t> dp(n, INT64_MAX - INT32_MAX);
    std::vector<int> parent(n, -1);
    dp[0] = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j){
            for (int k = 0; k < n; ++k) {
                if (dp[k] > dp[j] + graph[j][k] and graph[j][k] != INT32_MAX - W_MAX) {
                    dp[k] = dp[j] + graph[j][k];
                    parent[k] = j;
                }
            }
        }
    }
    std::vector<int> ans;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (dp[j] > dp[i] + graph[i][j] and graph[i][j] != INT32_MAX - W_MAX) {
                std::cout << "YES\n";
                for (int k = 0; k < 2 * n; ++k) {
                    j = parent[j];
                }
                i = j;
                while (i != parent[j]) {
                    ans.push_back(j);
                    j = parent[j];
                }
                ans.push_back(j);
                std::reverse(ans.begin(), ans.end());
                std::cout << ans.size() << std::endl;
                for (int v : ans) {
                    std::cout << v + 1 << " ";
                }
                std::cout << std::endl;
                return 0;
            }
        }
    }
    std::cout << "NO\n";
    return 0;
}
