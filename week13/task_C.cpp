#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
 
const int INF = int(1e7) + 1;
 
std::vector<bool> visited;
std::vector<int> prev;
std::vector<std::vector<int>> graph;
std::map<std::pair<int, int>, std::pair<int, int>> edges;
int n;
 
bool bfs() {
    visited.assign(n, 0);
    prev.assign(n, 0);
    std::queue<int> q;
    q.push(0);
    visited[0] = 1;
    prev[0] = -1;
    while (!q.empty()) {
        for (int i = 0; i < n; ++i) {
            if (!visited[i] and graph[q.front()][i] > 0) {
                visited[i] = 1;
                q.push(i);
                prev[i] = q.front();
            }
        }
        q.pop();
    }
    return visited[n - 1];
}
 
void dfs(int v) {
    visited[v] = 1;
    for (int i = 0; i < n; ++i) {
        if (!visited[i] and graph[v][i]) {
            dfs(i);
        }
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    
    int m;
    std::cin >> n >> m;
    graph.resize(n, std::vector<int>(n, 0));
    int a, b, c;
    for (int i = 0; i < m; ++i) {
        std::cin >> a >> b >> c;
        --a, --b;
        edges[{a, b}] = {i + 1, c};
        edges[{b, a}] = {i + 1, c};
        graph[a][b] = c;
        graph[b][a] = c;
    }
    while (bfs()) {
        int flow = INF;
        for (int i = n - 1; i != 0; i = prev[i]) {
            flow = std::min(flow, graph[prev[i]][i]);
        }
        for (int i = n - 1; i != 0; i = prev[i]) {
            graph[prev[i]][i] -= flow;
            graph[i][prev[i]] += flow;
        }
    }
    visited.assign(n, 0);
    dfs(0);
    int vol = 0;
    std::vector<int> vols;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::pair<int, int> cur = edges[{i, j}];
            if (visited[i] and !visited[j] and cur.second != 0) {
                vol += cur.second;
                vols.push_back(cur.first);
            }
        }
    }
    std::cout << vols.size() << ' ' << vol << '\n';
    for (int i : vols) {
        std::cout << i << ' ';
    }
 
    return 0;
}
