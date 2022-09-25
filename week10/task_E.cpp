#include <iostream>
#include <vector>
#include <set>
 
std::vector<std::vector<int>> graph;
std::vector<bool> used;
std::vector<int> time_enter, time_out;
std::set<int> answer;
int tick = 1;
 
void dfs(int v, int p) {
    used[v] = true;
    time_enter[v] = tick++;
    time_out[v] = time_enter[v];
    int cnt = 0;
    for (int u : graph[v]) {
        if (u == p) {
            continue;
        }
        if (used[u]) {
            time_out[v] = std::min(time_out[v], time_enter[u]);
        } else {
            dfs(u, v);
            time_out[v] = std::min(time_out[v], time_out[u]);
            if (time_out[u] >= time_enter[v] and p != -1) {
                answer.insert(v);
            }
            cnt += 1;
        }
    }
    if (p == -1 and cnt > 1) {
        answer.insert(v);
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m, beg, end;
    std::cin >> n >> m;
    graph.resize(n);
    for (int i = 0; i < m; ++i) {
        std::cin >> beg >> end;
        beg -= 1;
        end -= 1;
        graph[beg].push_back(end);
        graph[end].push_back(beg);
    }
    used.assign(n, false);
    time_enter.resize(n);
    time_out.resize(n);
    for (int i = 0; i < n; ++i) {
        if (!used[i]) {
            dfs(i, -1);
        }
    }
    std::cout << answer.size() << std::endl;
    for (int p : answer) {
        std::cout << p + 1 << " ";
    }
    std::cout << std::endl;
 
    return 0;
}
