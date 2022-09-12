#include <iostream>
#include <vector>
 
struct Node {
    Node* left;
    Node* right;
    int x, y, size;
    Node(int x): left(nullptr), right(nullptr), x(x),
                 y(rand() * RAND_MAX + rand()), size(1) {};
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
 
Node* merge(Node* t1, Node* t2) {
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
    if (get_size(t->left) < x) {
        split(t->right, x - get_size(t->left) - 1, t->right, t2);
        t1 = t;
    } else {
        split(t->left, x, t1, t->left);
        t2 = t;
    }
    update_size(t);
}
 
Node* add(Node* t, int pos, int x) {
    Node *t1, *t2;
    split(t, pos, t1, t2);
    Node* new_tree = new Node(x);
    return merge(merge(t1, new_tree), t2);
}
 
Node* remove(Node* t, int pos) {
    Node *t1, *t2, *t3, *t4;
    split(t, pos, t1, t2);
    split(t2, 1, t3, t4);
    t = merge(t1, t4);
    delete t3;
    return t;
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
        std::cin >> arr[i];
    }
 
    Node* tree = from_vector(arr);
 
    std::string operation;
    int ind, x;
    for (int i = 0; i < m; ++i) {
        std::cin >> operation;
        if (operation == "add") {
            std::cin >> ind >> x;
            tree = add(tree, ind, x);
        } else if (operation == "del") {
            std::cin >> ind;
            tree = remove(tree, ind - 1);
        }
    }
 
    std::cout << get_size(tree) << std::endl;
    print_tree(tree);
 
    return 0;
}
