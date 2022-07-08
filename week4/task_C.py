import sys


class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        # self.front = 0

    '''def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed'''

    def add(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[0]  # self.front
        # self.front -= 1
        # self.entries = self.entries[self.front:]
        self.entries = self.entries[1:]
        return dequeued


class CircularQueue:
    def __init__(self):
        self.capacity = 1
        self.array = [None] * self.capacity
        self.head = 0  # head pointer
        self.tail = 0  # tail pointer
        self.size = 0

    @staticmethod
    def _create_array(length):
        return [None] * length

    def _expand(self, new_capacity):
        new_array = self._create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.tail = self.size
        self.capacity = new_capacity

    def _reduce(self, new_capacity):
        new_array = self._create_array(new_capacity)
        new_array[:self.size] = self.array[self.head:self.tail]
        self.array = new_array
        self.head = 0
        self.tail = self.size
        self.capacity = new_capacity

    def enqueue(self, element):
        if self.size == self.capacity:
            self._expand(2 * self.capacity)  # expand array
        self.array[self.tail] = element
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return self

    def dequeue(self):
        element = None
        if self.size > 0:
            element = self.array[self.head]
            self.array[self.head] = None
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            if self.size <= self.capacity // 4:
                self._reduce(self.capacity // 2)  # reduce array
        return element


class CircularQueue2:
    def __init__(self):
        self.capacity = 4
        self.array = [None] * self.capacity
        self.front = 0  # index of the first element
        self.rear = 0
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def enqueue(self, data):
        if self.size >= self.capacity:
            raise Exception("QUEUE IS FULL")
        self.array[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            raise Exception("UNDERFLOW")
        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return temp


queue = CircularQueue2()
m = int(sys.stdin.readline())
for _ in range(m):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == '+':
        queue.enqueue(int(cmd[1]))  # add element
    elif cmd[0] == '-':
        print(queue.dequeue())  # get element
    print(queue.array)

# Input:
# 4
# + 1
# + 10
# -
# -
# Output:
# 1
# 10
