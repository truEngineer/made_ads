#include <iostream>
#include <cstddef>
 
 
struct Node {
    int key;
    int value;
    
    explicit Node(const int &key, const int &value) {
        this->key = key;
        this->value = value;
    }
};
 
 
class HashSet {
private:
    Node** htable;
    bool* dflags;
    
public:
    const size_t SIZE = int(2e6);  // hash table maximum size M = 2 * n
    const size_t PRIME = int(3e6) + 17;  // prime number P > M
 
    HashSet() {
        htable = new Node*[SIZE];
        dflags = new bool[SIZE];
        for(size_t i = 0; i < SIZE; ++i) {
            htable[i] = nullptr;
            dflags[i] = false;
        }
    }
    
    ~HashSet() {
        for (size_t i = 0; i < SIZE; ++i)
            delete htable[i];
        delete[] htable;
        delete[] dflags;
    }
 
    size_t hash_func(const int &key) {
        return ((17 * key) % PRIME) % SIZE;  // family ((A * x) % P) % M
    }
    
    bool insert(const int &key, const int &value) {
        size_t val = hash_func(key);
        size_t start = val;
        size_t end = (start > 0) ? ((start - 1) % SIZE) : SIZE - 1;
        while (start != end) {
            if (htable[start] == nullptr) {
                break;
            } else if (htable[start] != nullptr && htable[start]->key == key) {
                return false;
            }
            start = (start + 1) % SIZE;
        }
        if (start == end) {
            return false;
        }
        htable[start] = new Node(key, value);
        dflags[start] = false;
        return true;
    }
    
    Node* get(const int &key) {
        size_t val = hash_func(key);
        size_t start = val;
        size_t end = (start > 0) ? ((start - 1) % SIZE) : SIZE - 1;
        while (start != end) {
            if (htable[start] == nullptr && !dflags[start]) {
                return nullptr;
            } else if (htable[start] != nullptr && htable[start]->key == key) {
                return htable[start];
            }
            start = (start + 1) % SIZE;
        }
        return nullptr;
    }
    
    bool exists(const int &key) {
        return (get(key) != nullptr);
    }
    
    void delete_key(const int &key) {
        size_t val = hash_func(key);
        size_t start = val;
        size_t end = (start > 0) ? ((start - 1) % SIZE) : SIZE - 1;
        while (start != end) {
            if (htable[start] == nullptr && !dflags[start]) {
                return;
            } else if (htable[start] != nullptr && htable[start]->key == key) {
                int val = htable[start]->value;
                delete htable[start];
                htable[start] = nullptr;
                dflags[start] = true;
                return;
            }
            start = (start + 1) % SIZE;
        }
    }
};
 
 
int main() {
    std::ios::sync_with_stdio(false);
 
    HashSet set;
    while (!std::cin.eof()) {
        std::string operation;
        int key;
        std::cin >> operation >> key;
        if (operation == "insert") {
            set.insert(key, key);
        } else if (operation == "delete") {
            set.delete_key(key);
        } else if (operation == "exists") {
            std::cout << (set.exists(key) ? "true" : "false") << std::endl;
        }
    }
 
    return 0;
}
