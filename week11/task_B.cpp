#include <iostream>
#include <vector>
#include <set>
 
struct Edge {
    int to, w;
};
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<Edge>> graph(n);
    int beg, end, w;
    for (int i = 0; i < m; ++i) {
        std::cin >> beg >> end >> w;
        graph[beg - 1].push_back({end - 1, w});
        graph[end - 1].push_back({beg - 1, w});
    }
    std::vector<int64_t> dp(n, INT64_MAX);
    std::set<std::pair<int64_t, int>> q; // queue
    dp[0] = 0;
    q.insert({0, 0});
    while (!q.empty()) {
        auto [dst, u] = *(q.begin());
        q.erase({dst, u});
        for (auto [v, w] : graph[u]) {
            if (dp[v] > dp[u] + w) {
                if (dp[v] != INT64_MAX) {
                    q.erase({dp[v], v});
                }
                dp[v] = dp[u] + w;
                q.insert({dp[v], v});
            }
        }
    }
    for (auto dst : dp){
        std::cout << dst << " ";
    }
    std::cout << "\n";
 
    return 0;
}
