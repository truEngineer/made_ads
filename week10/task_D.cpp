
#include <iostream>
#include <vector>
#include <set>
 
std::vector<std::vector<int>> graph, trgraph;
std::vector<bool> used;
std::vector<int> ord, comp;
int cnt = 0;
 
void dfs_gr(int v) {
    used[v] = true;
    for (int u : graph[v]) {
        if (!used[u]) {
            dfs_gr(u);
        }
    }
    ord.push_back(v);
}
 
void dfs_tr(int v) {
    used[v] = true;
    comp[v] = cnt;
    for (int u : trgraph[v]) {
        if (!used[u]) {
            dfs_tr(u);
        }
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m, beg, end;
    std::cin >> n >> m;
    graph.resize(n);
    trgraph.resize(n);
    for (int i = 0; i < m; ++i) {
        std::cin >> beg >> end;
        beg -= 1;
        end -= 1;
        trgraph[beg].push_back(end);
        graph[end].push_back(beg);
    }
    used.resize(n, false);
    comp.resize(n, 0);
    for (int i = 0; i < n; ++i) {
        if (!used[i]) {
            dfs_gr(i);
        }
    }
    used.assign(n, false);
    for (int i = n - 1; i >= 0; --i) {
        if (!used[ord[i]]) {
            cnt += 1;
            dfs_tr(ord[i]);
        }
    }
    std::set<std::pair<int, int>> answer;
    for (int v = 0; v < n; ++v) {
        for (int u : trgraph[v]) {
            if (comp[v] != comp[u]) {
                answer.insert(std::make_pair(comp[v], comp[u]));
            }
        }
    }
    std::cout << answer.size() << std::endl;
 
    return 0;
}
