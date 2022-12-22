#include <iostream>
#include <algorithm>
#include <vector>

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
};

template<typename T>
std::istream &operator>>(std::istream &in, point_t<T> &p) {
    return in >> p.x >> p.y;
}

typedef long long ll;
typedef point_t<ll> point;

struct segment {
    point p1, p2;

    bool contains(point const &p) const {
        ll x1 = p1.x, y1 = p1.y;
        ll x2 = p2.x, y2 = p2.y;
        if (x2 < x1) {
            std::swap(x1, x2);
        }
        if (y2 < y1) {
            std::swap(y2, y1);
        }
        return (x1 <= p.x && p.x <= x2 && y1 <= p.y && p.y <= y2);
    }
};

bool inside(std::vector<point> const &polygon, point const &p) {
    bool count = false;
    for (int i = 0; i < polygon.size(); ++i) {
        int j = (i > 0 ? i - 1 : polygon.size() - 1);
        point p1 = polygon[j];
        point p2 = polygon[i];
        if (p2.y < p1.y) {
            std::swap(p1, p2);
        }
        ll rotate = (p2 - p1) / (p - p1);
        if (rotate == 0 && segment{p1, p2}.contains(p)) {
            return true;
        }
        if (p1.y == p2.y || p.y == std::min(p1.y, p2.y)) {
            continue;
        } else if (rotate > 0 && p1.y < p.y && p.y <= p2.y) {
            count ^= true;
        }
    }
    return count;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int n;
    point p0;
    std::cin >> n >> p0;
    std::vector<point> points(n);
    for (point &p : points) {
        std::cin >> p;
    }
    std::cout << (inside(points, p0) ? "YES\n" : "NO\n");

    return 0;
}
