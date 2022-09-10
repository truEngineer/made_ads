#include <iostream>
 
struct Node {
    Node* left;
    Node* right;
    int x;
    int y;
    Node(int x): left(nullptr), right(nullptr), 
                 x(x), y(rand() * RAND_MAX + rand()) {};
};
 
Node* root;
 
std::pair<Node*, Node*> split(Node* t, int k) {
    if(!t) {
        return {nullptr, nullptr};
    }
    if (k > t->x) {
        auto tmp = split(t->right, k);
        t->right = tmp.first;
        return {t, tmp.second};
    }
    auto tmp = split(t->left, k);
    t->left = tmp.second;
    return {tmp.first, t};
}
 
Node* merge(Node* a, Node* b) {
    if (!a) {
        return b;
    }
    if (!b) {
        return a;
    }
    if (a->y > b->y) {
        a->right = merge(a->right, b);
        return a;
    }
    b->left = merge(a, b->left);
    return b;
}
 
Node* insert(Node* t, Node* k) {
    auto tmp = split(t, k->x);
    tmp.first = merge(tmp.first, k);
    return merge(tmp.first, tmp.second);
}
 
Node* find(Node* v, int k) {
    if (!v) {
        return v;
    }
    if (v->x == k) {
        return v;
    }
    return (k > v->x) ? find(v->right, k) : find(v->left, k);
}
 
Node* remove(int x) {
    auto a = split(root, x);
    auto b = split(a.second, x + 1);
    return merge(a.first, b.second);
}
 
bool exists(int x) {
    return find(root, x);
}
 
Node* get_next(Node* v, int k) {
    if (!v) {
        return v;
    }
    if (k < v->x) {
        auto nd = get_next(v->left, k);
        return nd ? nd : v;
    }
    return get_next(v->right, k);
}
 
Node* get_prev(Node* v, int k) {
    if (!v) {
        return v;
    }
    if (k > v->x) {
        auto nd = get_prev(v->right, k);
        return nd ? nd : v;
    }
    return get_prev(v->left, k);
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    root = nullptr;
    int x;
    std::string operation;
    while (std::cin >> operation) {
        std::cin >> x;
        if (operation == "insert") {
            root = insert(root, new Node(x));
        } else if (operation == "delete") {
            root = remove(x);
        } else if (operation == "exists") {
            std::cout << (exists(x) ? "true" : "false") << std::endl;
        } else if (operation == "next") {
            auto next = get_next(root, x);
            std::cout << (next ? std::to_string(next->x) : "none") << std::endl;
        } else if (operation == "prev") {
            auto prev = get_prev(root, x);
            std::cout << (prev ? std::to_string(prev->x) : "none") << std::endl;
        }
    }
 
    return 0;
}
