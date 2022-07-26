#include <iostream>
#include <vector>
#include <cmath>
 
 
struct Node {
    std::string key;
    std::string value;
    Node* next;
    Node* linked_prev;
    Node* linked_next;
 
    explicit Node(std::string key, std::string value, Node* prev, Node* next) {
        this->key = key;
        this->value = value;
        this->next = nullptr;
        this->linked_prev = prev;
        this->linked_next = next;
    }
};
 
 
struct LinkedMap {
    const unsigned SIZE = int(1e5);
    const unsigned PRIME = int(2e5) + 3;
    
    std::vector<Node*> htable;
    Node* head;
    Node* linked_next;
    Node* linked_prev;
 
    LinkedMap() {
        htable.resize(SIZE);
        head = new Node("none", "none", nullptr, nullptr);
        head->linked_prev = head;
        head->linked_next = head;
        linked_next = nullptr;
        linked_prev = nullptr;
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
        Node* node = new Node(key, value, head->linked_prev, head);
        head->linked_prev->linked_next = node;
        node->next = htable[h % SIZE];
        htable[h % SIZE] = node;
        head->linked_prev = node;
    }
 
    std::string next(const std::string &key) {
        Node* node = get_value(key);
        return node == nullptr ? "none" : node->linked_next->value;
    }
 
    std::string prev(const std::string &key) {
        Node* node = get_value(key);
        return node == nullptr ? "none" : node->linked_prev->value;
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
                node->linked_next->linked_prev = node->linked_prev;
                node->linked_prev->linked_next = node->linked_next;
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
 
    LinkedMap lmap;
    while (!std::cin.eof()) {
        std::string operation;
        std::string key;
        std::cin >> operation >> key;
        if (operation == "put") {
            std::string value;
            std::cin >> value;
            lmap.put(key, value);
        } else if (operation == "delete") {
            lmap.delete_key(key);
        } else if (operation == "get") {
            std::cout << lmap.get(key) << std::endl;
        } else if (operation == "prev") {
            std::cout << lmap.prev(key) << std::endl;
        } else if (operation == "next") {
            std::cout << lmap.next(key) << std::endl;
        }
    }
    
    return 0;
}
