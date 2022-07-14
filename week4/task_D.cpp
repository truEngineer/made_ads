#include <iostream>
#include <cstdio>
#include <vector>
 
 
struct heapElement {
    int value;
    int number;
    
    heapElement() : value(0), number(0) {}
    heapElement(int v, int n) : value(v), number(n) {}
 
    bool operator<(const heapElement& other) const {
        return this->value < other.value;
    }
 
    bool operator==(int other) const {
        return this->number == other;
    }
 
    heapElement& operator=(int other) {
        this->value = other;
        return *this;
    }
};
 
 
template <typename T> 
class PriorityQueue {
 
    std::vector<T> heap;
 
    int search_ind(int key) {
        int ind = 0;
        for (int i = 0; i < heap.size(); i++) {
            if (heap[i] == key) {
                ind = i;
                break;
            }
        }
        return ind;
    }
 
    void sift_up(int i) {
        while (true) {
            int parent = i == 0 ? 0 : (i - 1) / 2;
            if (heap[i] < heap[parent]) {
                std::swap(heap[i], heap[parent]);
                i = parent;
            }
            else
                break;
        }
    }
 
    void sift_down(int i) {
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        int smallest = i;
        if (l < heap.size() && heap[l] < heap[i])
            smallest = l;
        if (r < heap.size() && heap[r] < heap[smallest])
            smallest = r;
        if (smallest != i) {
            std::swap(heap[i], heap[smallest]);
            sift_down(smallest);
        }
    }
 
public:
 
    bool extract_min(T& min) {
        if (heap.empty())
            return false;
        min = heap[0];
        std::swap(heap[0], heap[heap.size() - 1]);
        heap.pop_back();
        sift_down(0);
        return true;
    }
 
    void push(T element) {
        heap.push_back(element);
        sift_up(heap.size() - 1);
    }
 
    void decrease_key(int key, int new_value) {
        int ind = search_ind(key);
        heap[ind] = new_value;
        sift_up(ind);
    }
 
};
 
 
int main() {
 
    std::ios::sync_with_stdio(false);
 
    PriorityQueue<heapElement> pqueue;
    int op_number = 0;
 
    while (!std::cin.eof()) {
        op_number += 1;
        std::string operation;
        std::cin >> operation;
        if (operation == "push") {
            int key;
            std::cin >> key;
            pqueue.push(heapElement(key, op_number));
        }
        else if (operation == "extract-min") {
            heapElement min_key;
            if (pqueue.extract_min(min_key))
                std::cout << min_key.value << " " << min_key.number << "\n";
            else
                std::cout << "*" << "\n";
        }
        else if (operation == "decrease-key") {
            int number, value;
            std::cin >> number >> value;
            pqueue.decrease_key(number, value);
        }
    }
 
    return 0;
}
