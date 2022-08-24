#include <iostream>
#include <algorithm>
#include <vector>
 
const int64_t MAX_VAL = int64_t(1e18);
const int MAX_OP = 1 << 18;
 
struct Node {
    int64_t min;
    int64_t add;
    bool set;
};
 
std::vector<Node> arr_t(MAX_OP);
 
void push(int i) {
    if (arr_t[i].set) {
        arr_t[2 * i + 1] = arr_t[2 * i + 2] = {arr_t[i].min, 0, true};
        arr_t[i].set = false;
        return;
    }
    if (arr_t[i].add) {
        arr_t[2 * i + 1].min += arr_t[i].add;
        arr_t[2 * i + 2].min += arr_t[i].add;
        arr_t[2 * i + 1].add += (1 - arr_t[2 * i + 1].set) * arr_t[i].add;
        arr_t[2 * i + 2].add += (1 - arr_t[2 * i + 2].set) * arr_t[i].add;
        arr_t[i].add = 0;
        return;
    }
}
 
void update_add(int tl, int tr, int v, int l, int r, int64_t x) {
    if (tr <= l || r <= tl)
        return;
    if (l >= tl && r <= tr) {
        arr_t[v].min += x;
        if (!arr_t[v].set)
            arr_t[v].add += x;
        return;
    }
    push(v);
    int m = (l + r) / 2;
    update_add(tl, tr, 2 * v + 1, l, m, x);
    update_add(tl, tr, 2 * v + 2, m, r, x);
    arr_t[v].min = std::min(arr_t[2 * v + 1].min, arr_t[2 * v + 2].min);
}
 
void update_set(int tl, int tr, int v, int l, int r, int64_t x) {
    if (tr <= l || r <= tl)
        return;
    if (l >= tl && r <= tr) {
        arr_t[v] = {x, 0, true};
        return;
    }
    push(v);
    int m = (l + r) / 2;
    update_set(tl, tr, 2 * v + 1, l, m, x);
    update_set(tl, tr, 2 * v + 2, m, r, x);
    arr_t[v].min = std::min(arr_t[2 * v + 1].min, arr_t[2 * v + 2].min);
}
 
int64_t get_min(int tl, int tr, int v, int l, int r) {
    if (tr <= l || r <= tl)
        return MAX_VAL;
    if (l >= tl && r <= tr)
        return arr_t[v].min;
    push(v);
    int m = (l + r) / 2;
    int64_t min_l = get_min(tl, tr, 2 * v + 1, l, m);
    int64_t min_r = get_min(tl, tr, 2 * v + 2, m, r);
    return std::min(min_l, min_r);
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n;
    std::cin >> n;
 
    int pow_of_two = 1;
    while (pow_of_two < n)
        pow_of_two *= 2;
 
    int64_t t;
    for (int i = pow_of_two - 1; i < pow_of_two + n - 1; ++i) {
        std::cin >> t;
        arr_t[i] = {t, 0, false};
    }
 
    for (int i = pow_of_two + n - 1; i < 2 * pow_of_two - 1; ++i)
        arr_t[i] = {MAX_VAL, 0, false};
 
    for (int i = pow_of_two - 2; i >= 0; --i)
        arr_t[i] = {std::min(arr_t[2 * i + 1].min, arr_t[2 * i + 2].min), 0, false};
 
    std::string operation;
    int ind_i, ind_j;
    int64_t val;
    while (std::cin >> operation) {
        std::cin >> ind_i >> ind_j;
        int tl = ind_i + pow_of_two - 2; 
        int tr = ind_j + 1 + pow_of_two - 2;
        int l = pow_of_two - 1; 
        int r = 2 * pow_of_two - 1;
        if (operation == "set") {
            std::cin >> val;
            update_set(tl, tr, 0, l, r, val);
        } else if (operation == "add") {
            std::cin >> val;
            update_add(tl, tr, 0, l, r, val);
        } else if (operation == "min") {
            std::cout << get_min(tl, tr, 0, l, r) << std::endl;
        }
    }
 
    return 0;
}
