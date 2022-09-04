#include <iostream>
 
struct Node {
    int key;
    int height;
    Node* left;
    Node* right;
 
    explicit Node(int key): key(key), height(1), 
                            left(nullptr), right(nullptr) {}
 
    Node* rightRotate() {
        Node* n = this->left;
        this->left = n->right;
        n->right = this;
        this->updateHeight();
        n->updateHeight();
        return n;
    }
 
    Node* leftRotate() {
        Node* n = this->right;
        this->right = n->left;
        n->left = this;
        this->updateHeight();
        n->updateHeight();
        return n;
    }
 
    Node* rlRotate() {
        this->right = this->right->rightRotate();
        return this->leftRotate();
    }
 
    Node* lrRotate() {
        this->left = this->left->leftRotate();
        return this->rightRotate();
    }
 
    void updateHeight() {
        this->height = 1 + std::max(getHeight(this->left), getHeight(this->right));
    }
 
    static int getHeight(Node* n) {
        return !n ? 0 : n->height;
    }
 
    int getBalance() {
        return getHeight(this->left) - getHeight(this->right);
    }
};
 
struct AVLTree {
    Node* head;
 
    explicit AVLTree(): head(nullptr) {}
 
    void insert(int key) {
        this->head = insert(this->head, key);
    }
 
    static Node* insert(Node* root, int key) {
        if (!root) {
            return new Node(key);
        }
        if (key == root->key) {
            return root;
        }
        if (key < root->key) {
            root->left = insert(root->left, key);
        } else if (key > root->key) {
            root->right = insert(root->right, key);
        }
        root->updateHeight();
        int balance = root->getBalance();
        if (balance > 1 && key < root->left->key) {  // left-left
            return root->rightRotate();
        }
        if (balance < -1 && key > root->right->key) {  // right-right
            return root->leftRotate();
        }
        if (balance > 1 && key > root->left->key) {  // left-right
            return root->lrRotate();
        }
        if (balance < -1 && key < root->right->key) {  // right-left
            return root->rlRotate();
        }
        return root;
    }
 
    void remove(int key) {
        this->head = remove(this->head, key);
    }
 
    static Node* remove(Node* root, int key) {
        if (!root) {
            return nullptr;
        }
        if (key < root->key) {
            root->left = remove(root->left, key);
        } else if (key > root->key) {
            root->right = remove(root->right, key);
        } else {
            int sum = !root->left + !root->right;
            Node* removed;
            if (sum == 2) {  // no children
                removed = root;
                root = nullptr;
                delete removed;
            } else if (sum == 1) {  // one child
                removed = root;
                root = !root->left ? root->right : root->left;
                delete removed;
            } else if (sum == 0) {  // two children
                root->right = remove(root->right, (root->key = min(root->right)));
            }
        }
        if (!root) {
            return root;
        }
        root->height = 1 + std::max(Node::getHeight(root->left), Node::getHeight(root->right));
        int balance = root->getBalance();
        if (balance > 1 && root->left->getBalance() >= 0) {  // left-left
            return root->rightRotate();
        }
        if (balance > 1 && root->left->getBalance() < 0) {  // left-right
            return root->lrRotate();
        }
        if (balance < -1 && root->right->getBalance() <= 0) {  // right-right
            return root->leftRotate();
        }
        if (balance < -1 && root->right->getBalance() > 0) {  // right-left
            return root->rlRotate();
        }
        return root;
    }
 
    bool exists(int key) {
        return exists(this->head, key);
    }
 
    static bool exists(Node* root, int key) {
        while (root && root->key != key) {
            root = root->key > key ? root->left : root->right;
        }
        return root;
    };
 
    std::string next(int key) {
        Node* n = next(this->head, key);
        return !n ? "none" : std::to_string(n->key);
    }
 
    Node* next(Node* root, int key) {
        if (!root) {
            return nullptr;
        }
        Node* n = next(root->key > key ? root->left : root->right, key);
        return !n ? (root->key > key ? root : nullptr) : n;
    }
 
    std::string prev(int key) {
        Node* n = prev(this->head, key);
        return !n ? "none" : std::to_string(n->key);
    }
 
    Node* prev(Node* root, int key) {
        if (!root) {
            return nullptr;
        }
        Node* n = prev(root->key < key ? root->right : root->left, key);
        return !n ? (root->key < key ? root : nullptr) : n;
    }
 
    static int min(Node* v) {
        while (v->left) {
            v = v->left;
        }
        return v->key;
    }
};
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int x;
    AVLTree avlt;
    std::string operation;
    while (std::cin >> operation) {
        std::cin >> x;
        if (operation == "insert") {
            avlt.insert(x);
        } else if (operation == "delete") {
            avlt.remove(x);
        } else if (operation == "exists") {
            std::cout << (avlt.exists(x) ? "true" : "false") << std::endl;
        } else if (operation == "next") {
            std::cout << avlt.next(x) << std::endl;
        } else if (operation == "prev") {
            std::cout << avlt.prev(x) << std::endl;
        }
    }
 
    return 0;
}
