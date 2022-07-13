#include <iostream>
#include <algorithm>
 
 
class PriorityQueue {
 
    int *queue;
    int tail;
    int head;
    int size;
    int capacity;
    
public:
 
    PriorityQueue() {
        tail = 0;
        head = 0;
        size = 0;
        capacity = 1;
        queue = new int[capacity];
	}
 
    ~PriorityQueue() {
        delete[] queue;
	}
 
    void ensureCapacityMax() {
        if (size == capacity)
            resize(2 * capacity);
    }
    
    void ensureCapacityMin() {
        if (size < capacity / 4)
            resize(capacity / 2);
    }
 
    void resize(int new_capacity) {
        int *temp = new int[new_capacity];
        if (size > 0) {
            if (head < tail) {
                std::copy(queue + head, queue + (head + size), temp);
            } else {
                std::copy(queue + head, queue + capacity, temp);
                std::copy(queue, queue + tail, temp + (capacity - head));
            }
        }
        delete[] queue;
        queue = temp;
 
        head = 0;
        tail = (size == new_capacity) ? 0 : size;
        capacity = new_capacity;
    }
    
    void enqueue(int item) {
        ensureCapacityMax();
        queue[tail] = item;
        tail = (tail + 1) % capacity;
        size++;
    }
    
    int dequeue() {
        if (isEmpty()) {
            std::cout << "Queue size is ";
            return 0;
        }
        ensureCapacityMin();
        int item = queue[head];
        queue[head] = 0;
        head = (head + 1) % capacity;
        size--;
        return item;
	}
 
    bool isEmpty() {
        return size == 0;
    }
 
};
 
 
int main() {
 
    PriorityQueue pqueue;
    int m;
    std::cin >> m;
    char command;
 
    for (int i = 0; i < m; ++i) {
        std::cin >> command;
        if (command == '+') {
            int item;
            std::cin >> item;
            pqueue.enqueue(item);
        } else if (command == '-') {
            std::cout << pqueue.dequeue() << std::endl;
        }
    }
 
    return 0;
}
