#include <iostream>
 
struct Node {
    int64_t key;
    int64_t min, max;
    int64_t sum, height;
    Node* left;
    Node* right;
 
    explicit Node(int64_t k): key(k), min(k), max(k), sum(0), 
                              height(1), left(nullptr), right(nullptr) {}
 
    int64_t get_height_left() {
        if (!left) {
            return 0;
        } else {
            return left->height;
        }
    }
 
    int64_t get_height_right() {
        if (!right) {
            return 0;
        } else {
            return right->height;
        }
    }
 
    int64_t get_balance() {
        return get_height_right() - get_height_left();
    }
 
    int64_t get_sum_left() {
        if (left) {
            return left->sum;
        }
        return 0;
    }
 
    int64_t get_sum_right() {
        if (right) {
            return right->sum;
        }
        return 0;
    }
 
    int64_t get_min_left() {
        if (left) {
            return left->min;
        }
        return LLONG_MAX;
    }
 
    int64_t get_min_right() {
        if (right) {
            return right->min;
        }
        return LLONG_MAX;
    }
 
    int64_t get_max_left() {
        if (left) {
            return left->max;
        }
        return LLONG_MIN;
    }
 
    int64_t get_max_right() {
        if (right) {
            return right->max;
        }
        return LLONG_MIN;
    }
 
    void recalc_min_max() {
        this->min = std::min(std::min(get_min_left(), get_min_right()), key);
        this->max = std::max(std::max(get_max_left(), get_max_right()), key);
    }
 
    void recalc_sum() {
        sum = get_sum_left() + get_sum_right();
        if (left) {
            sum += left->key;
        }
        if (right) {
            sum += right->key;
        }
    }
 
    void recalc() {
        height = 1 + std::max(this->get_height_left(), this->get_height_right());
    }
};
 
Node* find(Node* cur_node, int val) {
    if (!cur_node || cur_node->key == val) {
        return cur_node;
    }
    if (cur_node->key < val) {
        return find(cur_node->right, val);
    } else {
        return find(cur_node->left, val);
    }
}
 
bool exists(Node* cur_node, int64_t val) {
    return find(cur_node, val);
}
 
Node* right_rotate(Node* cur_node) {
    Node* left = cur_node->left;
    cur_node->left = left->right;
    left->right = cur_node;
    cur_node->recalc();
    cur_node->recalc_sum();
    cur_node->recalc_min_max();
    left->recalc();
    left->recalc_sum();
    left->recalc_min_max();
    return left;
}
 
Node* left_rotate(Node* cur_node) {
    Node* right = cur_node->right;
    cur_node->right = right->left;
    right->left = cur_node;
    cur_node->recalc();
    cur_node->recalc_sum();
    cur_node->recalc_min_max();
    right->recalc();
    right->recalc_sum();
    right->recalc_min_max();
    return right;
}
 
Node* rebalance(Node* cur_node) {
    if (cur_node->get_balance() == 2) {
        if (cur_node->right->get_balance() < 0) {
            cur_node->right = right_rotate(cur_node->right);
        }
        return left_rotate(cur_node);
    }
    if (cur_node->get_balance() == -2) {
        if (cur_node->left->get_balance() > 0) {
            cur_node->left = left_rotate(cur_node->left);
        }
        return right_rotate(cur_node);
    }
    return cur_node;
}
 
Node* insert(Node* cur_node, int64_t new_key) {
    if (!cur_node) {
        return new Node(new_key);
    }
    if (new_key < cur_node->key) {
        cur_node->left = insert(cur_node->left, new_key);
    } else {
        cur_node->right = insert(cur_node->right, new_key);
    }
    cur_node->recalc();
    cur_node->recalc_sum();
    cur_node->recalc_min_max();
    return rebalance(cur_node);
}
 
Node* insert_node(Node* cur_node, int64_t new_key) {
    if (exists(cur_node, new_key)) {
        return cur_node;
    }
    return insert(cur_node, new_key);
}
 
int64_t sum(Node* cur_node, int64_t l, int64_t r) {
    if (!cur_node) {
        return 0;
    }
    if (cur_node->key > r) {
        return sum(cur_node->left, l, r);
    }
    if (cur_node->key < l) {
        return sum(cur_node->right, l, r);
    }
    if (!cur_node->left && !cur_node->right) {
        return cur_node->key;
    }
    if (cur_node->min >= l && cur_node->max <= r) {
        return cur_node->sum + cur_node->key;
    }
    return sum(cur_node->left, l, r) + sum(cur_node->right, l, r) + cur_node->key;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    Node* root = nullptr;
    char prev = '+';
    int64_t res = 0;
    int64_t n;
    std::cin >> n;
    for (int64_t i = 0; i < n; ++i) {
        char c;
        std::cin >> c;
        if (c == '+') {
            int64_t x;
            std::cin >> x;
            if (prev == '?') {
                root = insert_node(root, (x + res) % int(1e9));
            } else {
                root = insert_node(root, x);
            }
        } else {
            int64_t l, r;
            std::cin >> l >> r;
            res = sum(root, l, r);
            std::cout << res << std::endl;
        }
        prev = c;
    }
 
    return 0;
}
