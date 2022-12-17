#include <iostream>
#include <algorithm>
#include <cmath>
 
template<typename T>
struct point_t {
    T x, y;
 
    T operator^(point_t const &other) const {
        return x * other.y - y * other.x;
    }
 
    point_t operator-(point_t const &other) const {
        return point_t{x - other.x, y - other.y};
    }
};
 
template<typename T>
std::istream &operator>>(std::istream &in, point_t<T> &p) {
    return in >> p.x >> p.y;
}
 
typedef point_t<int> point;
 
struct segment {
    point p1, p2;
 
    bool contains(point const &p) const {
        int x1 = p1.x, y1 = p1.y;
        int x2 = p2.x, y2 = p2.y;
        if (x2 < x1) {
            std::swap(x1, x2);
        }
        if (y2 < y1) {
            std::swap(y2, y1);
        }
        return (x1 <= p.x && p.x <= x2 && y1 <= p.y && p.y <= y2);
    }
};
 
int sign(int const &value) {
    return (value == 0 ? 0 : (value > 0 ? 1 : -1));
}
 
int orientation(point const &top, point const &a, point const &b) {
    return (a - top) ^ (b - top);
}
 
int over_segment(segment const &s1, segment const &s2) {
    int sign1 = sign(orientation(s1.p1, s1.p2, s2.p1));
    int sign2 = sign(orientation(s1.p1, s1.p2, s2.p2));
    if (sign1 == 0 && sign2 == 0) {
        return 0;
    } else {
        return sign1 == sign2 ? 1 : -1;
    }
}
 
bool intersects(segment const &s1, segment const &s2) {
    int over_s1 = over_segment(s1, s2);
    int over_s2 = over_segment(s2, s1);
    if (over_s1 == -1 && over_s2 == -1) {
        return true;
    } else if (over_s1 == 1 || over_s2 == 1) {
        return false;
    } else {
        return s1.contains(s2.p1) || s1.contains(s2.p2) || s2.contains(s1.p1) || s2.contains(s1.p2);
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    point p1, p2, p3, p4;
    std::cin >> p1 >> p2;
    std::cin >> p3 >> p4;
    std::cout << (intersects(segment{p1, p2}, segment{p3, p4}) ? "YES\n" : "NO\n");
 
    return 0;
}
