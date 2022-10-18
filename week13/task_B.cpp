#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <iomanip>
 
int const INF = INT_MAX;
 
struct Edge {
    int u, v, f, c;
};
 
int n, m, s, t;
std::vector<Edge> edges;
std::vector<std::vector<int>> graph;
std::vector<int> d, p;
 
void add_edges(int u, int v, int c) {
    graph[u].push_back(edges.size());
    edges.push_back({u, v, 0, c});
    graph[v].push_back(edges.size());
    edges.push_back({v, u, 0, 0});
}
 
bool bfs() {
    std::fill(d.begin(), d.end(), -1);
    d[s] = 0;
    std::queue<int> q;
    q.push(s);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int e : graph[u]) {
            auto [_, v, f, c] = edges[e];
            if (f < c and d[v] == -1) {
                d[v] = d[u] + 1;
                q.push(v);
            }
        }
    }
    return d[t] != -1;
}
 
int dfs(int u, int min_c) {
    if (u == t or min_c == 0) {
        return min_c;
    }
    for (; p[u] < graph[u].size(); ++p[u]) {
        int e = graph[u][p[u]];
        auto [_, v, f, c] = edges[e];
        if (d[v] != d[u] + 1) {
            continue;
        }
        int pushed = dfs(v, std::min(min_c, c - f));
        if (pushed) {
            edges[e].f += pushed;
            edges[e ^ 1].f -= pushed;
            return pushed;
        }
    }
    return 0;
}
 
double max_flow() {
    double ans = 0;
    while (bfs()) {
        std::fill(p.begin(), p.end(), 0);
        while (int cur_flow = dfs(s, INF)) {
            ans += cur_flow;
        }
    }
    return ans;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    std::cin >> n >> m;
    graph.resize(n);
    d.resize(n);
    p.resize(n);
    s = 0;
    t = n - 1;
    int a, b, c;
    for (int i = 0; i < m; ++i) {
        std::cin >> a >> b >> c;
        a -= 1;
        b -= 1;
        add_edges(a, b, c);
        add_edges(b, a, c);
    }
    std::cout << std::setprecision(10) << max_flow() << '\n';
    for (int e = 0; e < edges.size(); e += 4) {
        double flow = edges[e].f;
        if (flow == 0) {
            flow = -edges[e + 2].f;
        }
        std::cout << std::setprecision(10) << flow << '\n';
    }
 
    return 0;
}
