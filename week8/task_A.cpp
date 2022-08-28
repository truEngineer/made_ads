#include <iostream>
 
struct Node {
    int key;
    Node* left;
    Node* right;
    Node(int x): key(x), left(nullptr), right(nullptr) {}
};
 
Node* insert(Node* n, int x) {
    if (!n) {
        return new Node(x);
    }
    if (n->key > x) {
        n->left = insert(n->left, x);
    } else if (n->key < x) {
        n->right = insert(n->right, x);
    }
    return n;
}
 
Node* min(Node* n) {
    if (!n->left) {
        return n;
    }
    return min(n->left);
}
 
Node* max(Node* n) {
    if (!n->right) {
        return n;
    }
    return max(n->right);
}
 
Node* erase(Node* n, int x) {
    if (n == nullptr) {
        return nullptr;
    }
    if (n->key == x) {
        if ((n->left) && (n->right)) {
            n->key = (min(n->right))->key;
            n->right = erase(n->right, n->key);
        } else if (n->left) {
            n = n->left;
        } else if (n->right) {
            n = n->right;
        } else {
            n = nullptr;
        }
    } else if (n->key > x) {
        n->left = erase(n->left, x);
    } else if (n->key < x) {
        n->right = erase(n->right, x);
    }
    return n;
}
 
Node* find(Node* n, int x) {
    if (!n) {
        return nullptr;
    }
    if (n->key == x) {
        return n;
    }
    if (n->key > x) {
        return find(n->left, x);
    } else if (n->key < x) {
        return find(n->right, x);
    }
    return nullptr;
}
 
Node* next(Node* n, int x) {
    Node* i = n;
    Node* j = nullptr;
    while (i) {
        if (i->key > x) {
            j = i;
            i = i->left;
        } else {
            i = i->right;
        }
    }
    return j;
}
 
Node* prev(Node* n, int x) {
    Node* i = n;
    Node* j = nullptr;
    while (i) {
        if (i->key < x) {
            j = i;
            i = i->right;
        } else {
            i = i->left;
        }
    }
    return j;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    
    int x;
    Node* root = nullptr;
    std::string operation;
    while (std::cin >> operation) {
        std::cin >> x;
        if (operation == "insert") {
            root = insert(root, x);
        } else if (operation == "delete") {
            root = erase(root, x);
        } else if (operation == "exists") {
            std::cout << (find(root, x) ? "true" : "false") << std::endl;
        } else if (operation == "next") {
            Node* n = next(root, x);
            std::cout << (n ? std::to_string(n->key) : "none") << std::endl;
        } else if (operation == "prev") {
            Node* n = prev(root, x);
            std::cout << (n ? std::to_string(n->key) : "none") << std::endl;
        }
    }
 
    return 0;
}
