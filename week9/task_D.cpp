#include <iostream>
#include <vector>
 
struct Node {
    Node* left;
    Node* right;
    int x, y, size;
    bool rev;
    Node(int x): left(nullptr), right(nullptr), size(1), x(x),
                 y(rand() * RAND_MAX + rand()), rev(false) {};
};
 
int get_size(Node* t) {
    if (!t) {
        return 0;
    }
    return t->size;
}
 
void update_size(Node* t) {
    if (!t) {
        return; 
    }
    t->size = 1 + get_size(t->left) + get_size(t->right);
}
 
void push(Node*& t) {
    if (t && t->rev) {
        t->rev = false;
        std::swap(t->left, t->right);
        if (t->left) {
            t->left->rev ^= true;
        }
        if (t->right) {
            t->right->rev ^= true;
        }
    }
}
 
Node* merge(Node* t1, Node* t2) {
    push(t1);
    push(t2);
    if (!t1) {
        return t2;
    }
    if (!t2) {
        return t1;
    }
    if (t1->y > t2->y) {
        t1->right = merge(t1->right, t2);
        update_size(t1);
        return t1;
    } else {
        t2->left = merge(t1, t2->left);
        update_size(t2);
        return t2;
    }
}
 
void split(Node* t, int x, Node*& t1, Node*& t2) {
    if (!t) {
        t1 = nullptr;
        t2 = nullptr;
        return;
    }
    push(t);
    if (get_size(t->left) < x) {
        split(t->right, x - get_size(t->left) - 1, t->right, t2);
        t1 = t;
    } else {
        split(t->left, x, t1, t->left);
        t2 = t;
    }
    update_size(t);
}
 
Node* reverse_query(Node* t, int l, int r) {
    Node *t1, *t2, *t3;
    split(t, l, t1, t2);
    split(t2, r - l + 1, t2, t3);
    t2->rev ^= true;
    return merge(merge(t1, t2), t3);
}
 
Node* from_vector(const std::vector<int>& vec) {
    Node* res = nullptr;
    for (int i = 0; i < vec.size(); ++i) {
        res = merge(res, new Node(vec[i]));
    }
    return res;
}
 
void print_tree(Node* t) {
    if (!t) { 
        return;
    }
    push(t);
    print_tree(t->left);
    std::cout << t->x << " ";
    print_tree(t->right);
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m;
    std::cin >> n >> m;
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        arr[i] = i + 1;
    }
 
    Node* tree = from_vector(arr);
 
    int l, r;
    for (int i = 0; i < m; ++i) {
        std::cin >> l >> r;
        tree = reverse_query(tree, l - 1, r - 1);
    }
 
    print_tree(tree);
 
    return 0;
}
