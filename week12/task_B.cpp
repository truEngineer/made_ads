#include <iostream>
#include <algorithm>
#include <vector>

struct Set {
    int exp, rank, main;
};

std::vector<Set> sets;

int find(int a) {
    while (sets[a].main != a) {
        a = sets[a].main;
    }
    return a;
}

int get(int a) {
    if (sets[a].main != a) {
        return sets[a].exp + get(sets[a].main);
    }
    return sets[a].exp;
}

void join(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b)
        return;
    if (sets[b].rank > sets[a].rank) {
        std::swap(a, b);
    }
    sets[b].main = a;
    sets[b].exp -= sets[a].exp;
    sets[a].rank = std::max(sets[a].rank, sets[b].rank + 1);
}

void add(int a, int v) {
    a = find(a);
    sets[a].exp += v;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int n, m, a, b;
    std::cin >> n >> m;
    sets.resize(n);
    for (int i = 0; i < n; ++i) {
        sets[i] = {0, 0, i};
    }
    std::string op;
    for (int i = 0; i < m; ++i) {
        std::cin >> op;
        if (op == "get") {
            std::cin >> a;
            std::cout << get(a - 1) << '\n';
        } else if (op == "join") {
            std::cin >> a >> b;
            join(a - 1, b - 1);
        } else if (op == "add") {
            std::cin >> a >> b;
            add(a - 1, b);
        }
    }

    return 0;
}
