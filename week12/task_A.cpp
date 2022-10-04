#include <iostream>
#include <algorithm>
#include <vector>
 
struct Set {
    int main, min, max, cnt;
};
 
std::vector<Set> sets;
 
int find(int a) {
    if (sets[a].main != a) {
        return sets[a].main = find(sets[a].main);
    }
    return a;
}
 
void join(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) {
        return;
    }
    sets[a].min = std::min(sets[a].min, sets[b].min);
    sets[a].max = std::max(sets[a].max, sets[b].max);
    sets[a].cnt += sets[b].cnt;
    sets[b].main = a;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie();
 
    int n, a, b;
    std::cin >> n;
    sets.resize(n);
    for (int i = 0; i < n; ++i) {
        sets[i] = {i, i, i, 1};
    }
    std::string op;
    while (std::cin >> op) {
        if (op == "union") {
            std::cin >> a >> b;
            join(a - 1, b - 1);
        } else if (op == "get") {
            int a;
            std::cin >> a;
            a = find(a - 1);
            std::cout << sets[a].min + 1 << ' ' << sets[a].max + 1 << ' ' << sets[a].cnt << '\n';
        }
    }
 
    return 0;
}
