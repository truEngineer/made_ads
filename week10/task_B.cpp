#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
 
std::map<std::string, std::vector<std::string>> adj_list;
std::map<std::string, bool> visited;
 
int dfs(std::string s) {
    if (visited[s]) {
        return 0;
    }
    visited[s] = true;
    int cnt = 0;
    for (auto u : adj_list[s]) {
        cnt = std::max(dfs(u), cnt);
    }
    return cnt + 1;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n;
    std::cin >> n;
    std::string name1, name2, rep;
    for (int i = 0; i < n; ++i) {
        std::cin >> name1 >> rep >> name2;
        std::transform(name1.begin(), name1.end(), name1.begin(), ::tolower);
        std::transform(name2.begin(), name2.end(), name2.begin(), ::tolower);
        adj_list[name2].push_back(name1);
        adj_list[name1].push_back(name2);
    }
    std::cout << dfs("polycarp") << std::endl;
 
    return 0;
}
