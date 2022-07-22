#include <iostream>
#include <vector>
#include <cmath>
 
 
struct Node {
    std::string key;
    std::string value;
    Node* next;
 
    explicit Node(int hash, std::string key, std::string value) {
        this->key = key;
        this->value = value;
        this->next = nullptr;
    }
};
 
 
struct Map {
    const unsigned SIZE = int(1e5);
    const unsigned PRIME = int(2e5) + 3;
 
    std::vector<Node*> htable;
 
    Map() {
        htable.resize(SIZE);
    }
 
    int hash(const std::string& s) {
        unsigned long long sum = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            sum += pow(31, i) * s[i];
        }
        unsigned long long hash = (sum % PRIME) % SIZE;
        return static_cast<int>(hash);
    }
 
 
    void put(const std::string &key, const std::string &value) {
        Node* x = get_value(key);
        if (x != nullptr) {
            x->value = value;
            return;
        }
        int h = hash(key);
        Node* node = new Node(h, key, value);
        node->next = htable[h % SIZE];
        htable[h % SIZE] = node;
    }
 
    Node* get_value(const std::string &key) {
        Node* node = htable[hash(key) % SIZE];
        while (node != nullptr) {
            if (node->key == key) {
                return node;
            }
            node = node->next;
        }
        return nullptr;
    }
 
    std::string get(const std::string &key) {
        Node* node = get_value(key);
        return node == nullptr ? "none" : node->value;
    }
 
    void delete_key(const std::string &key) {
        int h = hash(key);
        Node* node = htable[h % SIZE];
        Node* prev_node = nullptr;
        while (node != nullptr) {
            if (node->key == key) {
                if (prev_node == nullptr) {
                    htable[h % SIZE] = node->next;
                } else {
                    prev_node->next = node->next;
                    node->next = nullptr;
                }
                return;
            }
            prev_node = node;
            node = node->next;
        }
    }
};
 
 
int main() {
    std::ios::sync_with_stdio(false);
 
    Map map;
    while (!std::cin.eof()) {
        std::string operation;
        std::string key;
        std::cin >> operation >> key;
        if (operation == "put") {
            std::string value;
            std::cin >> value;
            map.put(key, value);
        } else if (operation == "delete") {
            map.delete_key(key);
        } else if (operation == "get") {
            std::cout << map.get(key) << std::endl;
        }
    }
 
    return 0;
}
