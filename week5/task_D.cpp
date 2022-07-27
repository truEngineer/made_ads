#include <iostream>
#include <vector>
 
 
const unsigned int OUTER_SIZE = 10000;
const unsigned int INNER_SIZE = 10;
 
 
unsigned int hash(const std::string &x, const int mod) {
    unsigned int res = 0;
    for (size_t i = 0; i < x.size(); ++i) {
        res *= 31;
        res += x[i] + 7 * (i & 1);
    }
    return res % mod;
}
 
 
struct NodeTable {
    std::vector<std::vector<std::pair<std::string, bool>>> table;
    size_t size;
 
    NodeTable() {
        this->table.resize(INNER_SIZE);
        this->size = 0;
    }
 
    void insert(const std::string &val) {
        unsigned int x = hash(val, INNER_SIZE);
        for (auto &i : table[x]) {
            if (i.first == val) {
                if (!i.second) {
                    this->size++;
                    i.second = true;
                }
                return;
            }
        }
        this->size++;
        table[x].emplace_back(val, true);
    }
 
    void remove(const std::string &val) {
        unsigned int x = hash(val, INNER_SIZE);
        for (auto &i : table[x]) {
            if (i.first == val) {
                if (i.second) {
                    this->size--;
                    i.second = false;
                }
                return;
            }
        }
    }
 
    void clear() {
        this->size = 0;
        this->table.clear();
    }
 
    void print() {
        std::cout << this->size;
        for (auto &i : table) {
            for (auto &j : i) {
                if (j.second) {
                    std::cout << " " << j.first;
                }
            }
        }
        std::cout << std::endl;
    }
};
 
 
struct MultiMap {
    std::vector<std::vector<std::pair<std::string, NodeTable>>> table;
 
    MultiMap() {
        this->table.resize(OUTER_SIZE);
    }
 
    NodeTable* find(const std::string &key, unsigned int x) {
        for (auto &i : table[x]) {
            if (i.first == key) {
                return &i.second;
            }
        }
        return nullptr;
    }
 
    void put(const std::string &key, const std::string &val) {
        unsigned int x = hash(key, OUTER_SIZE);
        NodeTable *element = find(key, x);
        if (element != nullptr) {
            element->insert(val);
        } else {
            NodeTable tmp;
            tmp.insert(val);
            table[x].emplace_back(key, tmp);
        }
    }
 
    void delete_key(const std::string &key, const std::string &val) {
        unsigned int x = hash(key, OUTER_SIZE);
        NodeTable *element = find(key, x);
        if (element != nullptr) {
            element->remove(val);
        }
    }
 
    void delete_all(const std::string &key) {
        unsigned int x = hash(key, OUTER_SIZE);
        NodeTable *element = find(key, x);
        if (element != nullptr) {
            element->clear();
        }
    }
 
    void get(const std::string &key) {
        unsigned int x = hash(key, OUTER_SIZE);
        NodeTable *element = find(key, x);
        if (element != nullptr) {
            element->print();
        } else {
            std::cout << "0" << std::endl;
        }
    }
};
 
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
 
    MultiMap map;
    while (!std::cin.eof()) {
        std::string operation, key, value;
        std::cin >> operation >> key;
        if (operation == "put") {
            std::cin >> value;
            map.put(key, value);
        } else if (operation == "delete") {
            std::cin >> value;
            map.delete_key(key, value);
        } else if (operation == "deleteall") {
            map.delete_all(key);
        } else if (operation == "get") {
            map.get(key);
        }
    }
    
    return 0;
}
