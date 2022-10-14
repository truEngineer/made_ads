#include <iostream>
#include <algorithm>
#include <vector>
 
struct Edge {
    int u, v, w;
};
 
std::vector<Edge> edges;
std::vector<int> p;
 
int find(int a) {
    if (p[a] != a) {
        return p[a] = find(p[a]);
    }
    return a;
}
 
void join(int a, int b) {
    a = find(a);
    b = find(b);
    p[b] = a;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m;
    std::cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        int b, e, w;
        std::cin >> b >> e >> w;
        edges.push_back({b - 1, e - 1, w});
    }
    std::sort(edges.begin(), edges.end(), 
              [] (Edge e1, Edge e2) -> bool { return e1.w < e2.w; });
    p.resize(n);
    for (int i = 0; i < n; ++i) {
        p[i] = i;
    }
    int64_t ans = 0;
    for (auto [b, e, w] : edges) {
        if (find(b) == find(e)) {
            continue;
        }
        ans += w;
        join(b, e);
    }
    std::cout << ans;
 
    return 0;
}
