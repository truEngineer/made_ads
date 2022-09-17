#include <iostream>
#include <vector>
 
std::vector<std::vector<int>> adj_list;
std::vector<int> comp;
 
void dfs(int v, int num) {
    if (comp[v] != 0) {
        return;
    }
    comp[v] = num;
    for (int u : adj_list[v]) {
        dfs(u, num);
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m;
    std::cin >> n >> m;
    comp.resize(n, 0);
    adj_list.resize(n);
    int beg, end;
    while (m != 0) {
        std::cin >> beg >> end;
        beg -= 1;
        end -= 1;
        adj_list[beg].push_back(end);
        adj_list[end].push_back(beg);
        m -= 1;
    }
    int cnt = 1;
    while (n != 0) {
        if (comp[n - 1] == 0) {
            dfs(n - 1, cnt);
            cnt += 1;
        }
        n -= 1;
    }
    std::cout << cnt - 1 << std::endl;
    for (int c : comp) {
        std::cout << c << " ";
    }
    std::cout << std::endl;
 
    return 0;
}
