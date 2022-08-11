#include <iostream>
#include <vector>
 
template<class T>
class FenwickTree {
    std::vector<T> tree;
    T size;
public:
    FenwickTree(T size) {
        this->size = size;
        tree.assign(size, 0);
    }
 
    FenwickTree(std::vector<T> a): FenwickTree(a.size()) {
        for (size_t i = 0; i < a.size(); ++i) {
            set(i, a[i]);
        }
    }
 
    T sum(T r) {
        T res = 0;
        for (; r >= 0; r = (r & (r + 1)) - 1) {
            res += tree[r];
        }
        return res;
    }
 
    T sum(T l, T r) {
        return sum(r) - sum(l - 1);
    }
 
    void set(T idx, T delta) {
        for (; idx < size; idx = idx | (idx + 1)) {
            tree[idx] += delta;
        }
    }
};
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n;
    std::cin >> n;
    std::vector<int64_t> arr_a(n);
    for (size_t i = 0; i < n; ++i) {
        std::cin >> arr_a[i];
    }
    auto fwt = FenwickTree<int64_t>(arr_a);
 
    std::string operation;
    int64_t op1, op2;
    while(std::cin >> operation) {
        std::cin >> op1 >> op2;
        if (operation == "set") {
            fwt.set(op1 - 1, op2 - arr_a[op1 - 1]);
            arr_a[op1 - 1] = op2;
        } else if (operation == "sum") {
            std::cout << fwt.sum(op1 - 1, op2 - 1) << std::endl;
        }
    }
 
    return 0;
}
