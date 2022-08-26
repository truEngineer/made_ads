#include <algorithm>
#include <iostream>
#include <vector>
 
const int SIZE = 1 << 17;
 
struct Query {
    int l, r;
    int64_t res;
};
 
bool compare(Query a, Query b) {
    return a.res < b.res;
}
 
std::vector<Query> arr_a;
std::vector<int64_t> tree(2 * SIZE - 1);
int pow_two;
 
void update_set(int tl, int tr, int v, int l, int r, int64_t x) {
    if (tr <= l || r <= tl)
        return;
    if (l >= tl && r <= tr) {
        tree[v] = x;
        return;
    }
    int m = (l + r) / 2;
    update_set(tl, tr, 2 * v + 1, l, m, x);
    update_set(tl, tr, 2 * v + 2, m, r, x);
}
 
int64_t result(int tl, int tr, int v, int l, int r) {
    if (tr <= l || r <= tl)
        return LLONG_MAX;
    if (l >= tl && r <= tr)
        return tree[v];
    int m = (l + r) / 2;
    int64_t minl = result(tl, tr, 2 * v + 1, l, m);
    int64_t minr = result(tl, tr, 2 * v + 2, m, r);
    return std::min(minl, minr);
}
 
void check(int v) {
    if (tree[v] == LLONG_MAX)
        tree[v] = tree[(v - 1) / 2];
    if (tree[v] < tree[(v - 1) / 2])
        tree[v]  = tree[(v - 1) / 2];
}
 
void build(int v) {
    if (v >= pow_two - 1)
        return;
    if (tree[v] != LLONG_MAX) {
        check(2 * v + 1);
        check(2 * v + 2);
    }
    build(2 * v + 1);
    build (2 * v + 2);
}
 
 
int main() {
    freopen("rmq.in", "r", stdin);
    freopen("rmq.out", "w", stdout);
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m;
    std::cin >> n >> m;
 
    pow_two = 1;
    while (pow_two < n)
        pow_two *= 2;
 
    for (int i = 0; i < 2 * pow_two - 1; ++i)
        tree[i] = LLONG_MAX;
 
    int x1, x2;
    int64_t val;
    for (int i = 0; i < m; ++i) {
        std::cin >> x1 >> x2 >> val;
        arr_a.push_back({x1, x2, val});
    }
    sort(arr_a.begin(), arr_a.end(), compare);
 
    for (int i = 0; i < m; ++i)
        update_set(arr_a[i].l + pow_two - 2, arr_a[i].r + pow_two - 1, 0, pow_two - 1, 2 * pow_two - 1, arr_a[i].res);
 
    build(0);
 
    for (int i = pow_two - 2; i >= 0; --i)
        tree[i] = std::min(tree[2 * i + 1], tree[2 * i + 2]);
 
    bool cons = true;
    for (int i = 0; i < m && cons; ++i) {
        val = result(arr_a[i].l + pow_two - 2, arr_a[i].r + pow_two - 1, 0, pow_two - 1, 2 * pow_two - 1);
        if (val != arr_a[i].res)
            cons = false;
    }
    if (cons) {
        std::cout << "consistent" << std::endl;
        for (int i = pow_two - 1; i < pow_two + n - 1; ++i)
            if (tree[i] == LLONG_MAX)
                std::cout << INT_MAX << " ";
            else
                std::cout << tree[i] << " ";
    } else
        std::cout << "inconsistent";
    
    std::cout << std::endl;
 
    return 0;
}
