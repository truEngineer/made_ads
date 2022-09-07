#include <iostream>
 
struct Node {
    int key, height, size;
    Node* left;
    Node* right;
    Node(int key): key(key), height(1), size(0),
                   left(nullptr), right(nullptr) {}
};
 
int size(Node* p) {
    return !p ? -1 : p->size;
}
 
void correct_size(Node* p) {
    p->size = size(p->left) + size(p->right) + 2;
}
 
int height(Node* p) {
    return !p ? 0 : p->height;
}
 
void correct_height(Node* p) {
    p->height = (height(p->left) > height(p->right) ? height(p->left) : height(p->right)) + 1;
}
 
int balance_differents(Node* p) {
    return height(p->right) - height(p->left);
}
 
Node* rotate_left(Node* p) {
    Node* right = p->right;
    p->right = right->left;
    right->left = p;
    correct_size(p);
    correct_size(right);
    correct_height(p);
    correct_height(right);
    return right;
}
 
Node* rotate_right(Node* p) {
    Node* left = p->left;
    p->left = left->right;
    left->right = p;
    correct_size(p);
    correct_size(left);
    correct_height(p);
    correct_height(left);
    return left;
}
 
Node* balance(Node* p) {
    correct_size(p); 
    correct_height(p);
    if (balance_differents(p) == 2) {
        if (balance_differents(p->right) < 0) {
            p->right = rotate_right(p->right);
        }
        return rotate_left(p);
    }
    if (balance_differents(p) == -2) {
        if (balance_differents(p->left) > 0) {
            p->left = rotate_left(p->left);
        }
        return rotate_right(p);
    }
    return p;
}
 
Node* find_k(Node* p, int k) {
    if (!p->right) {
        return (k == 1) ? p : find_k(p->left, k - 1);
    }
    if (k == 2 + size(p->right)) {
        return p;
    }
    if (k > 2 + size(p->right)) {
        return find_k(p->left, k - 2 - size(p->right));
    }
    return find_k(p->right, k);
}
 
Node* insert(Node* p, int key) {
    if (!p) {
        return new Node(key);
    }
    if (p->key > key) {
        p->left = insert(p->left, key);
    } else {
        p->right = insert(p->right, key);
    }
    correct_size(p);
    correct_height(p);
    return balance(p);
}
 
Node* find_min(Node* p) {
    return !p->left ? p : find_min(p->left);
}
 
Node* remove_min(Node* p) {
    if (!p->left) {
        return p->right;
    }
    p->left = remove_min(p->left);
    correct_size(p);
    correct_height(p);
    return balance(p);
}
 
Node* remove(Node* p, int key) {
    if (!p) {
        return nullptr;
    }
    if (key < p->key) {
        p->left = remove(p->left, key);
        if (p->left) {
            correct_size(p->left);
            correct_height(p->left);
        }
    } else if (key > p->key) {
        p->right = remove(p->right, key);
        if (p->right) {
            correct_height(p->right);
            correct_size(p->right);
        }
    } else {
        Node* left_child = p->left;
        Node* right_child = p->right;
        if (!right_child) {
            return left_child;
        }
        Node* min = find_min(right_child);
        min->right = remove_min(right_child);
        min->left = left_child;
        correct_size(min);
        correct_height(min);
        return balance(min);
    }
    return balance(p);
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, c, k;
    std::cin >> n;
    Node *tree = nullptr;
    for (int i = 0; i < n; ++i) {
        std::cin >> c >> k;
        if (c == 1) {
            tree = insert(tree, k);
        } else if (c == 0) {
            std::cout << find_k(tree, k)->key << std::endl;
        } else if (c == -1) {
            tree = remove(tree, k);
        }
    }
 
    return 0;
}
