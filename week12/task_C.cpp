#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
 
struct Vertex {
    int x, y;
};
 
int dist(Vertex v1, Vertex v2) {
    auto [x1, y1] = v1;
    auto [x2, y2] = v2;
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, x, y;
    std::cin >> n;
    std::vector<Vertex> verts(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> x >> y;
        verts[i] = {x, y};
    }
    std::vector<bool> used(n, false);
    std::vector<int> min(n, INT_MAX);
    std::vector<int> end(n, -1);
    min[0] = 0;
    double ans = 0;
    for (int i = 0; i < n; ++i) {
        int u = -1;
        for (int j = 0; j < n; ++j) {
            if (!used[j] and (u == -1 or min[j] < min[u])) {
                u = j;
            }
        }
        used[u] = true;
        ans += u == 0 ? 0 : sqrt(dist(verts[u], verts[end[u]]));
        for (int v = 0; v < n; ++v) {
            if (dist(verts[u], verts[v]) < min[v]) {
                min[v] = dist(verts[u], verts[v]);
                end[v] = u;
            }
        }
    }
    std::cout << std::setprecision(11) << ans;
 
    return 0;
}
