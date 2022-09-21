#include <iostream>
#include <algorithm>
#include <vector>
 
std::vector<std::vector<int>> adj_list;
std::vector<int> color;
std::vector<int> answer;
bool cycle;
 
void dfs(int v) {
    if (color[v] == 2) {
        return;
    }
    color[v] = 1;
    for (int u : adj_list[v]) {
        if (color[u] == 1) {
            cycle = true;
            return;
        }
        dfs(u);
    }
    color[v] = 2;
    answer.push_back(v);
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m, beg, end;
    std::cin >> n >> m;
    adj_list.resize(n);
    color.resize(n);
    for (int i = 0; i < m; ++i) {
        std::cin >> beg >> end;
        adj_list[beg - 1].push_back(end - 1);
    }
    for (int i = 0; i < n; ++i) {
        dfs(i);
    }
    if (cycle) {
        std::cout << -1;
    } else {
        std::reverse(answer.begin(), answer.end());
        for (int v : answer) {
            std::cout << v + 1 << " ";
        }
    }
    std::cout << std::endl;
 
    return 0;
}
