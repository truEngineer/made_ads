#include <iostream>
 
struct Node {
    Node* left;
    Node* right;
    int x, y, size;
    Node(int x): left(nullptr), right(nullptr), x(x),
                 y(rand() * RAND_MAX + rand()), size(1) {}
};
 
Node* root;
 
int size(Node* t) {
    return t ? t->size : 0;
}
 
void update_size(Node* t) {
    t->size = size(t->left) + size(t->right) + 1;
}
 
std::pair<Node*, Node*> split(Node* t, int k) {
    if (!t) {
        return {nullptr, nullptr};
    }
    if (size(t->left) >= k) {
        std::pair<Node*, Node*> tmp = split(t->left, k);
        t->left = tmp.second;
        update_size(t);
        return {tmp.first, t};
    }
    std::pair<Node*, Node*> tmp = split(t->right, k - size(t->left) - 1);
    t->right = tmp.first;
    update_size(t);
    return {t, tmp.second};
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
        update_size(a);
        return a;
    }
    b->left = merge(a, b->left);
    update_size(b);
    return b;
}
 
void print_tree(Node* t) {
    if (!t) {
        return;
    }
    print_tree(t->left);
    std::cout << t->x << " ";
    print_tree(t->right);
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    root = nullptr;
    int n, m, l, r;
    std::cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        root = merge(root, new Node(i));
    }
    for (int i = 0; i < m; ++i) {
        std::cin >> l >> r;
        std::pair<Node*, Node*> tmp1 = split(root, l - 1);
        std::pair<Node*, Node*> tmp2 = split(tmp1.second, r - l + 1);
        root = merge(merge(tmp2.first, tmp1.first), tmp2.second);
    }
    print_tree(root);
 
    return 0;
}
