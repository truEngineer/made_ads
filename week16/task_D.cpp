#include <iostream>
#include <vector>
 
struct point {
    int x, y;
 
    point() : x(0), y(0) {}
 
    point(int const &x, int const &y) : x(x), y(y) {}
 
    point(point const &other) = default;
};
 
std::istream &operator>>(std::istream &in, point &p) {
    return in >> p.x >> p.y;
}
 
struct polygon {
    std::vector<point> verts;
    
    polygon(std::vector<point> v) : verts(std::move(v)) {}
 
    double area(int a, int b){
        return (verts[a].x - verts[b].x) * 
               (verts[a].y + verts[b].y) / 2.0;
    }
 
    double polygon_area() {
        double ans = 0;
        int n = verts.size();
        for (int i = 1; i < n; ++i)
            ans += area(i - 1, i);
        ans += area(n - 1, 0);
        if (ans < 0) 
            ans *= -1;
        return ans;
    }
};
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n;
    std::cin >> n;
    std::vector<point> points(n);
    for (point &p : points) {
        std::cin >> p;
    }
    polygon pol = polygon(points);
    double ans = pol.polygon_area();
    std::cout.precision(1);
    std::cout << std::fixed << ans << std::endl;
 
    return 0;
}
