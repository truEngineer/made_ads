#include <iostream>
#include <vector>
 
struct point {
    int x, y;
};
 
std::vector<point> polygon;
 
double area(int a, int b) {
    return (polygon[a].x - polygon[b].x) * 
           (polygon[a].y + polygon[b].y) / 2.0;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n;
    std::cin >> n;
    polygon.reserve(n);
    for (int i = 0; i < n; ++i)
        std::cin >> polygon[i].x >> polygon[i].y;
    double ans = 0;
    for (int i = 1; i < n; ++i)
        ans += area(i - 1, i);
    ans += area(n - 1, 0);
    if (ans < 0) 
        ans *= -1;
    std::cout.precision(1);
    std::cout << std::fixed << ans << std::endl;
 
    return 0;
}
