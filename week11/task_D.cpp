#include <iostream>
#include <vector>
 
struct Edge {
    int v;
    int64_t w;
};
 
std::vector<std::vector<Edge>> graph;
std::vector<bool> used;
 
void dfs(int v) {
    if (used[v]) {
        return;
    }
    used[v] = true;
    for (auto [u, w] : graph[v]) {
        dfs(u);
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m, s;
    std::cin >> n >> m >> s;
    graph.resize(n);
    int beg, end;
    int64_t w;
    for (int i = 0; i < m; ++i) {
        std::cin >> beg >> end >> w;
        graph[beg - 1].push_back({end - 1, w});
    }
    std::vector<int64_t> dp(n, INT64_MAX);
    dp[s - 1] = 0;
    for (int i = 0; i < n; ++i) {
        bool stop = true;
        for (int u = 0; u < n; ++u) {
            for (auto [v, w] : graph[u]) {
                if (dp[u] < INT64_MAX and dp[v] > dp[u] + w) {
                    dp[v] = dp[u] + w;
                    stop = false;
                }
            }
        }
        if (stop) {
            break;
        }
    }
    used.resize(n);
    for (int u = 0; u < n; ++u) {
        for (auto [v, w] : graph[u]) {
            if (dp[u] < INT64_MAX and dp[v] > dp[u] + w and !used[u]) {
                dfs(u);
            }
        }
    }
    for (int u = 0; u < n; ++u) {
        if (dp[u] == INT64_MAX) {
            std::cout << "*\n";
            continue;
        }
        if (used[u]) {
            std::cout << "-\n";
            continue;
        }
        std::cout << dp[u] << std::endl;
    }
 
    return 0;
}
