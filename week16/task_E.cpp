#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
 
template<typename T>
struct point_t {
    T x, y;
 
    point_t() : x(0), y(0) {}
 
    point_t(T const &x, T const &y) : x(x), y(y) {}
 
    point_t(point_t<T> const &other) = default;
 
    T operator/(point_t const &other) const {
        return x * other.y - y * other.x;
    }
 
    point_t operator-(point_t const &other) const {
        return point_t(x - other.x, y - other.y);
    }
 
    T sqr_length() const {
        return x * x + y * y;
    }
};
 
template<typename T>
std::istream &operator>>(std::istream &in, point_t<T> &p) {
    return in >> p.x >> p.y;
}
 
template<typename T>
std::ostream &operator<<(std::ostream &out, point_t<T> const &p) {
    return out << p.x << ' ' << p.y;
}
 
typedef long long ll;
typedef point_t<ll> point;
 
std::vector<point> convex_hull(std::vector<point> &points) {
    point p = *min_element(points.begin(), points.end(), [](point const &p1, point const &p2) {
        return p1.y < p2.y || (p1.y == p2.y && p1.x > p2.x);
    });
    std::sort(points.begin(), points.end(), [&p](point const &p1, point const &p2) {
        ll rotate = (p1 - p) / (p2 - p);
        return rotate > 0 || (rotate == 0 && (p1 - p).sqr_length() < (p2 - p).sqr_length());
    });
    std::vector<point> result{p};
    for (int i = 1; i < points.size(); ++i) {
        point next = points[i];
        while (result.size() >= 2) {
            point v_prev = result.back() - result[result.size() - 2];
            point v_next = next - result.back();
            ll rotate = v_next / v_prev;
            if (rotate >= 0) {
                result.pop_back();
            } else {
                break;
            }
        }
        result.push_back(next);
    }
    return result;
}
 
double length(point a, point b) {
    return sqrt((a - b).sqr_length());
}
 
double perimeter(std::vector<point> &points) {
    double per = 0;
    for (int i = 1; i < points.size(); ++i)
        per += length(points[i - 1], points[i]);
    per += length(points.back(), points[0]);
    return per;
}
 
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
    auto chull = convex_hull(points);
    std::cout << perimeter(chull) << '\n';
 
    return 0;
}
