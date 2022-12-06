#include <iostream>
#include <algorithm>
#include <cmath>
 
struct point {
    int x, y;
 
    point() : x(0), y(0) {}
 
    point(int const &x, int const &y) : x(x), y(y) {}
 
    point(point const &other) = default;
 
    int operator/(point const &other) const {
        return x * other.y - y * other.x;
    }
};
 
std::istream &operator>>(std::istream &in, point &p) {
    return in >> p.x >> p.y;
}
 
struct segment {
    point p1, p2;
 
    bool contains(point const &p) const {
        if ((p.x < p1.x && p.x < p2.x) || (p.y < p1.y && p.y < p2.y))
            return false;
        else if ((p.x > p1.x && p.x > p2.x) || (p.y > p1.y && p.y > p2.y))
            return false;
        else {
            double ans = abs((p / p1 + p1 / p2 + p2 / p) / 2.0);
            return ans == 0;
        }
    }
};
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    point p, p1, p2;
    std::cin >> p >> p1 >> p2;
    std::cout << (segment{p1, p2}.contains(p) ? "YES\n" : "NO\n");
    
    return 0;
}
