#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <iomanip>
 
struct Edge {
    int u, v, f, c;
};
 
int n, m, s, t;
std::vector<Edge> edges;
std::vector<std::vector<int>> graph;
std::vector<int> d, p;
 
void add_edges(int u, int v, int c = 1) {
    graph[u].push_back(edges.size());
    edges.push_back({u, v, 0, c});
    graph[v].push_back(edges.size());
    edges.push_back({v, u, 0, 0});
}
 
bool bfs() {
    fill(d.begin(), d.end(), -1);
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
    for (; p[u] < graph[u].size(); p[u]++) {
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
        while (int cur_flow = dfs(s, INT_MAX)) {
            ans += cur_flow;
        }
    }
    return ans;
}
 
void create_path(int u, std::vector<int>& path) {
    path.push_back(u);
    if (u == t) {
        return;
    }
    for (auto e : graph[u]) {
        auto [_, v, f, c] = edges[e];
        if (f != c or c == 0) {
            continue;
        }
        edges[e].f = edges[e + 1].f = 0;
        create_path(v, path);
        break;
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    std::cin >> n >> m >> s >> t;
    --s, --t;
    graph.resize(n);
    d.resize(n);
    p.resize(n);
    int x, y;
    for (int i = 0; i < m; ++i) {
        std::cin >> x >> y;
        add_edges(x - 1, y - 1);
    }
    double res = max_flow();
    if (res < 2) {
        std::cout << "NO";
        return 0;
    }
    std::vector<int> path1, path2;
    create_path(s, path1);
    create_path(s, path2);
    std::cout << "YES" << '\n';
    for (int e : path1) {
        std::cout << e + 1 << ' ';
    }
    std::cout << '\n';
    for (int e : path2) {
        std::cout << e + 1 << ' ';
    }
 
    return 0;
}
